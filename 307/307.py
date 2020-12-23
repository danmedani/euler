from copy import deepcopy
from typing import List
from typing import NamedTuple

class Ways(NamedTuple):
	total_ways: int
	ways_with_3_or_more_defects: int


hash_map = {}
def hash(defects_left: int, chip_defect_counts: List[int]) -> str:
	return str(defects_left) + '-'.join([str(count) for count in chip_defect_counts])


def distribute_defects(
	defects_left: int,
	ways_of_getting_here: int,
	chip_defect_counts: List[int] # e.g. [10, 2, 0, 1] means there are 10 chips with 0 defects, 2 chips with 1 defect, & 1 chip with 3 defects
) -> Ways:
	if defects_left == 0:
		return Ways(
			total_ways=ways_of_getting_here, 
			ways_with_3_or_more_defects=ways_of_getting_here if len(chip_defect_counts) > 3 else 0
		)


	hash_val = hash(defects_left, chip_defect_counts)
	if hash_val in hash_map:
		return hash_map[hash_val]


	total_ways = 0
	ways_with_3_or_more_defects = 0

	for defect_count in range(len(chip_defect_counts)):
		if chip_defect_counts[defect_count] == 0:
			# no chips available with this number of defects
			continue

		new_chip_defect_counts = deepcopy(chip_defect_counts)
		
		# the number of chips with defect_count should decrement since we're adding a defect to one of them
		new_chip_defect_counts[defect_count] -= 1

		# the number of chips with defect_count+1 just went up by 1
		if defect_count + 1 >= len(new_chip_defect_counts):
			new_chip_defect_counts.append(0)
		new_chip_defect_counts[defect_count + 1] += 1

		ways = distribute_defects(
			defects_left=defects_left - 1,
			ways_of_getting_here=ways_of_getting_here * chip_defect_counts[defect_count],
			chip_defect_counts=new_chip_defect_counts
		)
		total_ways += ways.total_ways
		ways_with_3_or_more_defects += ways.ways_with_3_or_more_defects


	result = Ways(
		total_ways=total_ways,
		ways_with_3_or_more_defects=ways_with_3_or_more_defects		
	)
	hash_map[hash_val] = result
	return result


# This returns what it should: ≈ 0.0204081633
total_ways, ways_with_3_or_more_defects = distribute_defects(defects_left=3, ways_of_getting_here=1, chip_defect_counts=[7])

# This maxes out recursion depth
# total_ways, ways_with_3_or_more_defects = distribute_defects(defects_left=20000, ways_of_getting_here=1, chip_defect_counts=[1000000])

print('total ways =', total_ways)
print('ways w 3+ defects =',  ways_with_3_or_more_defects)
print('chance of chip having 3+ defects =', 1.0 * ways_with_3_or_more_defects / total_ways)


