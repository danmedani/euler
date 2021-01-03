import random
import time
from typing import List
from typing import Dict
import math
from fractions import Fraction
from functools import lru_cache

MOD = 10 ** 9

def get_all_digit_number(digit_map: Dict[int, int]) -> int:
	val = 0
	ten_pow = 1
	for digit, digit_count in digit_map.items():
		while digit_count > 0:
			val += (ten_pow * digit)
			ten_pow *= 10
			digit_count -= 1
	return val


def get_permutation_count(digit_map: Dict[int, int]) -> int:
	num_length = sum([val for val in digit_map.values() if val > 0])
	perms = Fraction(math.factorial(num_length), 1)
	for digit_count in digit_map.values():
		perms = perms / math.factorial(digit_count)
	return perms.numerator


@lru_cache(maxsize=10000)
def get_d_mult(total_tail_perm_count: int, digit_count: int, total_tail_digit_count: int) -> int:
	return int(Fraction(total_tail_perm_count, 1) * Fraction(digit_count, total_tail_digit_count))

@lru_cache(maxsize=50)
def get_ten_pow(power: int) -> int:
	return 10 ** power

@lru_cache(maxsize=50)
def get_next_lowest_ten_pow(power: int) -> int:
	return int(power / 10)

def get_unique_num_sums_fast(digit_map: Dict[int, int], mod_val: int) -> int:
	num_length = sum(digit_map.values())
	the_sum = 0

	perm_time = 0
	loop_time = 0

	# select a first digit (that isn't 0)
	for first_digit in digit_map.keys():
		if first_digit == 0:
			continue
		# print('first_digit = {}'.format(first_digit))
		digit_map[first_digit] -= 1
		total_tail_perm_count = get_permutation_count(digit_map)
		total_tail_digit_count = sum([val for val in digit_map.values()])
		# print('total_tail_perm_count = {}'.format(total_tail_perm_count))

		ten_pow = get_ten_pow(num_length - 1)

		# count the first digit!
		the_sum += ((first_digit * total_tail_perm_count * ten_pow) % mod_val)

		# print('first digit sum = {}'.format(first_digit * total_tail_perm_count * ten_pow % mod_val))

		# count the rest
		ten_pow = get_next_lowest_ten_pow(ten_pow)
		if ten_pow == 0:
			# it was a 1 digit number
			continue

		# print('base_tail_show_count_per_digit = {}'.format(base_tail_show_count_per_digit))
		# print('digit_map = {}'.format(digit_map))
		if len([key for key in digit_map if digit_map[key] > 0]) == 1:
			the_sum += get_all_digit_number(digit_map)
		else:
			while ten_pow > 0:
				for digit, digit_count in digit_map.items():
					d_mult = get_d_mult(total_tail_perm_count, digit_count, total_tail_digit_count)
					the_sum += (ten_pow * digit * d_mult % mod_val)
				ten_pow = get_next_lowest_ten_pow(ten_pow)

		digit_map[first_digit] += 1

	return the_sum % mod_val


def get_unique_num_sums(
	digit_map: Dict[int, int],
	val_so_far: int,
	is_first_digit: bool,
	mod_val: int
) -> int:
	if sum(digit_map.values()) == 0:
		return val_so_far % mod_val

	the_sum = 0
	if is_first_digit:
		for digit in digit_map.keys():
			if digit != 0:
				digit_map[digit] -= 1
				the_sum += ( get_unique_num_sums(digit_map, val_so_far * 10 + digit, False, mod_val) % mod_val )
				digit_map[digit] += 1
	else:
		for (digit, digit_count) in digit_map.items():
			if digit_count > 0:
				digit_map[digit] -= 1
				the_sum += ( get_unique_num_sums(digit_map, val_so_far * 10 + digit, False, mod_val) % mod_val )
				digit_map[digit] += 1

	return the_sum % mod_val


def extract_digit_map(value: int) -> Dict[int, int]:
	digit_map = {}

	while value > 0:
		digit = value % 10
		if digit not in digit_map:
			digit_map[digit] = 0
		digit_map[digit] += 1
		value = int(value / 10)

	return digit_map


# x = 10**10
# while True:
# 	if x % 10 == 0:
# 		y = x + 5
# 		while x < y:
# 			print(x)
# 			if get_unique_num_sums_fast(extract_digit_map(x), MOD) != get_unique_num_sums(extract_digit_map(x), 0, True, MOD):
# 				print('ALERT', x)
# 				raise Exception('nope')
# 			x += 1
# 	else:
# 		print(x)
# 		if get_unique_num_sums_fast(extract_digit_map(x), MOD) != get_unique_num_sums(extract_digit_map(x), 0, True, MOD):
# 			print('ALERT', x)
# 			raise Exception('nope')
# 	x += random.randint(1, 1000000)

# x = 99999999999999999733
# print(get_unique_num_sums_fast(extract_digit_map(x), MOD))
# print(get_unique_num_sums(extract_digit_map(x), 0, True, MOD))

def get_unique_number_sets_that_sum_to(
	val_to_sum_to: int,
	max_digit: int,
	digits_left: int,
	val_so_far: int
) -> List[int]:
	if val_to_sum_to == 0 and digits_left == 0:
		return [val_so_far]

	if val_to_sum_to < 0:
		return []

	if digits_left * (max_digit ** 2) < val_to_sum_to:
		return []

	if digits_left == 0:
		return []

	res = []
	for next_digit in range(max_digit, -1, -1):
		for nexts in get_unique_number_sets_that_sum_to(
			val_to_sum_to=val_to_sum_to - (next_digit ** 2),
			max_digit=next_digit,
			digits_left=digits_left - 1,
			val_so_far=(val_so_far * 10) + next_digit
		):
			res.append(nexts)
	return res


for number_length in range(1, 5):
	print(number_length, get_unique_number_sets_that_sum_to(29, 9, number_length, 0))


# total_sum = 0
# total_og_sum = 0
# perm_time = 0
# loop_time = 0
# for square in range(1, 45):
# 	print('square', square)
# 	for number_length in range(1, 21):
# 		for unique_num_set in get_unique_number_sets_that_sum_to(
# 			val_to_sum_to=square * square, 
# 			max_digit=9,
# 			digits_left=number_length, 
# 			val_so_far=0
# 		):
# 			# print(unique_num_set)
# 			# print(get_unique_num_sums_fast(extract_digit_map(unique_num_set), MOD))
# 			total_sum += get_unique_num_sums_fast(extract_digit_map(unique_num_set), MOD)
# 			# perm_time += this_perm_time
# 			# loop_time += this_loop_time
# 			# total_og_sum += get_unique_num_sums(extract_digit_map(unique_num_set), 0, True, MOD)

# 	print(square, total_sum % MOD)
# 	# print(square, total_og_sum % MOD)

# print(total_sum % MOD)



