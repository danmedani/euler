from typing import Dict
from functools import lru_cache
from fractions import Fraction
from mypy_extensions import TypedDict
from typing import List
from typing import Optional


def concat_digits(min_digit: int, max_digit: int) -> int:
	return int(''.join([str(val) for val in list(range(min_digit, max_digit + 1))]))

@lru_cache(maxsize=1000)
def create_nodes(min_digit: int, max_digit: int):
	all_nodes = [
		{
			'val': None
		}	
	]
	for partition_start in range(min_digit, max_digit):
		for left_node in create_nodes(min_digit, partition_start):
			for right_node in create_nodes(partition_start + 1, max_digit):
				all_nodes.append(
					{
						'left': left_node,
						'right': right_node
					}
				)
	return all_nodes

def num_vals(nodes):
	vals = 0
	if 'val' in nodes:
		return 1
	return num_vals(nodes['right']) + num_vals(nodes['left'])


def concat_digits(min_digit: int, max_digit: int) -> int:
	return_val = 0
	for val in range(min_digit, max_digit + 1):
		return_val = (return_val * 10) + val
	return return_val


def get_all_values(min_digit: int, max_digit: int) -> List[List[int]]:
	# the one
	values = [[
		concat_digits(min_digit, max_digit)
	]]
	for end_of_first in range(min_digit, max_digit):
		first_val = concat_digits(min_digit, end_of_first)
		for rest_values in get_all_values(end_of_first + 1, max_digit):
			values.append(
				[first_val] + rest_values
			)
	return values


def get_templates(min_digit: int, max_digit: int) -> List[Dict]:
	node_dict = {}
	for node in create_nodes(min_digit, max_digit):
		if str(node) not in node_dict:
			node_dict[str(node)] = True

	return list([eval(node_dict_str) for node_dict_str in node_dict.keys()])


def inject_values(template, values):
	template_str = str(template)
	for value in values:
		template_str = template_str.replace('None', str(value), 1)
	return eval(template_str)

reachable_hash = {}

def all_reachable(node):
	hashed_node = str(node)
	if hashed_node in reachable_hash:
		return reachable_hash[hashed_node]

	if 'val' in node:
		return [
			Fraction(node['val'], 1)
		]

	all_vals = []
	left_vals = all_reachable(node['left'])
	right_vals = all_reachable(node['right'])
	for left_val in left_vals:
		for right_val in right_vals:
			all_vals.append(left_val + right_val)
			all_vals.append(left_val - right_val)
			all_vals.append(left_val * right_val)
			if right_val != 0:
				all_vals.append(left_val / right_val)
	
	reachable_hash[hashed_node] = all_vals
	return all_vals

def get_all_injected(min_digit: int, max_digit: int):
	templates = get_templates(min_digit, max_digit)
	all_values = get_all_values(min_digit, max_digit)

	all_of_em = []
	for values in all_values:
		len_values = len(values)
		for template in templates:
			if num_vals(template) == len_values:
				all_of_em.append(
					inject_values(template, values)
				)
	return all_of_em


min_digit = 1
max_digit = 9

all_injected = get_all_injected(min_digit, max_digit)

set_reachable = {}
for injected in all_injected:
	# print(injected)
	for reachable in [
		val 
		for val in all_reachable(injected)
		if val > 0 and val.denominator == 1
	]:
		set_reachable[reachable.numerator] = True

print(len(list(set_reachable.keys())))
print(sum(list(set_reachable.keys())))

