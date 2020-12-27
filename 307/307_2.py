import time
from fractions import Fraction
from typing import NamedTuple
from typing import Dict
from typing import List
from copy import deepcopy
from functools import lru_cache


def hash(chip_defect_counts: List[int]) -> str:
	return '-'.join([str(count) for count in chip_defect_counts])


@lru_cache(maxsize=25000)
def chip_pow(chips, defects_left):
	return chips ** defects_left

class Node(NamedTuple):
	ways: int
	chip_defect_counts: List[int]


DEFECTS = 20000
CHIPS = 1000000

total_ways = CHIPS ** DEFECTS
frac = Fraction(0, total_ways)


defects_left = DEFECTS

layer_hash_map: Dict[str, Node] = {
	'init': Node(
		ways=1,
		chip_defect_counts=[CHIPS]
	)
}

while defects_left >= 0:
	nodes = layer_hash_map.values()
	layer_hash_map = {}
	start_time = time.time()
	print()
	print('-|-')
	print('defects_left', defects_left, '  -- layer len: ', len(nodes))
	
	if defects_left % 500 == 0:
		print('frac', frac)

	if len(nodes) == 0:
		break

	count_p3_ways = 0

	total_pow_time = 0
	for node in nodes:
		if len(node.chip_defect_counts) > 3:
			count_p3_ways += node.ways
			continue

		for defect_count in range(len(node.chip_defect_counts)):
			if node.chip_defect_counts[defect_count] == 0:
				continue

			new_chip_defect_counts = deepcopy(node.chip_defect_counts)
			new_chip_defect_counts[defect_count] -= 1
			if defect_count + 1 >= len(new_chip_defect_counts):
				new_chip_defect_counts.append(0)
			new_chip_defect_counts[defect_count + 1] += 1
			
			next_node_hash = hash(new_chip_defect_counts)
			new_ways = node.ways * node.chip_defect_counts[defect_count]
			if next_node_hash not in layer_hash_map:
				layer_hash_map[next_node_hash] = Node(ways=new_ways, chip_defect_counts=new_chip_defect_counts)
			else:
				layer_hash_map[next_node_hash] = Node(ways=new_ways + layer_hash_map[next_node_hash].ways, chip_defect_counts=new_chip_defect_counts)
	
	pow_time = time.time()
	count_p3 = count_p3_ways * (CHIPS ** defects_left)
	total_pow_time += (time.time() - pow_time)

	frac += Fraction(count_p3, total_ways)
	defects_left -= 1

	print('total_pow_time: {}s'.format(total_pow_time))
	print('time taken: {}s'.format(time.time() - start_time))


print('end')
print('frac = ', frac)
print('total ways = ', total_ways)



