import math
from typing import List
from functools import lru_cache
from fractions import Fraction

# def magic_hash(dice_rolls_so_far: List[int], rolls: int, max_dice: int) -> str:
# 	# counts dupes, counts dupes with max_dice in it, etc
# 	return ''

def get_permutations(dice_rolls_so_far: List[int]) -> int:
	dupe_counts = []
	dice_roll_index = 0
	while dice_roll_index < len(dice_rolls_so_far) - 1:
		offset = 1
		while dice_roll_index + offset < len(dice_rolls_so_far) and dice_rolls_so_far[dice_roll_index] == dice_rolls_so_far[dice_roll_index + offset]:
			offset += 1

		if offset > 1:
			dupe_counts.append(offset)

		dice_roll_index += offset

	perms = Fraction(math.factorial(len(dice_rolls_so_far)), 1)
	for dupe_count in dupe_counts:
		perms = perms / math.factorial(dupe_count)
	return perms.numerator


# print(get_permutations([5, 5, 4, 3, 2, 1, 1, 1]))


def get_count(dice_rolls_so_far: List[int], rolls: int, max_dice: int) -> int:
	# hash_val = magic_hash(dice_rolls_so_far, rolls, max_dice)
	# if hash_val in get_combos_hash_map:
	# 	return get_combos_hash_map[hash_val]

	if rolls == 0:
		return get_permutations(dice_rolls_so_far)

	the_sum = 0
	for dice_roll in range(1, max_dice + 1):
		dice_rolls_so_far.append(dice_roll)
		the_sum += get_count(dice_rolls_so_far, rolls - 1, dice_roll)
		dice_rolls_so_far.pop()
	return the_sum


def get_top_rolls_count(dice_rolls_so_far: List[int], top_rolls: int, sum_needed: int, max_dice: int) -> int:
	if top_rolls == 0:
		if sum_needed != 0:
			return 0
		return get_count(dice_rolls_so_far, 10, max_dice)

	if max_dice * top_rolls < sum_needed:
		return 0

	if top_rolls > sum_needed:
		return 0

	the_sum = 0
	for dice_roll in range(1, max_dice + 1):
		dice_rolls_so_far.append(dice_roll)
		the_sum += get_top_rolls_count(dice_rolls_so_far, top_rolls - 1, sum_needed - dice_roll, dice_roll)
		dice_rolls_so_far.pop()
	return the_sum


print(get_top_rolls_count([], 10, 70, 12))
