from functools import lru_cache
from fractions import Fraction
from mypy_extensions import TypedDict
from typing import Optional


def eval(node) -> Fraction:
	if 'val' in node:
		return node['val']

	if node['operator'] == '*':
		return eval(node['left']) * eval(node['right'])
	elif node['operator'] == '/':
		return eval(node['left']) / eval(node['right'])
	elif node['operator'] == '+':
		return eval(node['left']) + eval(node['right'])
	elif node['operator'] == '-':
		return eval(node['left']) - eval(node['right'])

	raise Exception('wat')

def concat_digits(min_digit: int, max_digit: int) -> int:
	return int(''.join([str(val) for val in list(range(min_digit, max_digit + 1))]))

@lru_cache(maxsize=10000)
def create_nodes(min_digit: int, max_digit: int):
	all_nodes = [
		{
			'val': Fraction(concat_digits(min_digit, max_digit), 1)
		}	
	]
	for partition_start in range(min_digit, max_digit):
		for left_node in create_nodes(min_digit, partition_start):
			for right_node in create_nodes(partition_start + 1, max_digit):
				all_nodes = all_nodes + [
					{
						'operator': operator,
						'left': left_node,
						'right': right_node
					}
					for operator in ['*', '/', '+', '-']
				]
	return all_nodes

reachable = {}
nodes = create_nodes(3, 8)
for node in nodes:
	try:
		evaled_node = eval(node)
	except ZeroDivisionError:
		continue
	if evaled_node.denominator == 1 and evaled_node > Fraction(0, 1):
		reachable[evaled_node] = True

sum_reachable = 0
for reachable_item, _ in reachable.items():
	sum_reachable = sum_reachable + reachable_item
print(sum_reachable)
# print(42 in reachable)

# print(
# 	eval(
# 		{
# 			'operator': '*',
# 			'left': {
# 				'val': Fraction(5, 1)
# 			},
# 			'right': {
# 				'val': Fraction(4, 1)
# 			}
# 		}
# 	)
# )


