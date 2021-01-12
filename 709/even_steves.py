# 1234

# 3(12)4
# 24(13)
# 34(12)
# 14(23)

# cabinet [1, 2, 5, 6, 7]
# 		       |_>[3, 4]

# cabinet [2, 6, 7, 8]
#                   |_> [1, 5]
# 		                  |_>[3, 4]
# - keep ordered
# - to hash, just DFS with layer chars

# hash layer 1:
# generate all next layers, hash a layer 2
# repeat
from collections import defaultdict
from typing import Dict
from typing import List


# 0 -> [12, 6, 7, 8]
# 8 -> [1, 5]
# 5 -> [3, 4]

def pack(bag: int, cabinet: Dict[int, List[int]]) -> str:
	packing = []
	for a_bag in cabinet[bag]:
		packing.append(str(a_bag) + '|')
		if a_bag in cabinet:
			packing.append('(')
			packing.append(pack(a_bag, cabinet))
			packing.append(')')
	return ''.join(packing)


def unpack(packing: str) -> Dict[int, List[int]]:
	cabinet = {}
	bag_stack = [
		(0, 0, len(packing))
	]

	while bag_stack:
		current_bag, start, end = bag_stack.pop()
		cabinet[current_bag] = []
		index = start
		while index < end:
			if packing[index] != '(':
				if index == len(packing) - 1 and packing[index] == ')':
					index += 1
					continue

				number_end_index = index + 1
				while number_end_index < len(packing) and packing[number_end_index] != '|':
					number_end_index += 1
				cabinet[current_bag].append(int(packing[index:number_end_index]))
				index = number_end_index + 1
			elif packing[index] == '(':
				layers_deep = 0
				inner_bag_end = index + 1
				while packing[inner_bag_end] != ')' or layers_deep > 0:
					inner_bag_end += 1

					if packing[inner_bag_end] == '(':
						layers_deep += 1
					elif packing[inner_bag_end] == ')':
						layers_deep -=1
				bag_stack.append((cabinet[current_bag][-1], index + 1, inner_bag_end - 1))
				
				index = inner_bag_end + 1
			else:
				raise Exception('NOT SUPPOSED TO BE HERE!')

	return cabinet


print(pack(0, unpack(pack(0, {
	0: [1, 2, 3],
	3: [4, 5],
	5: [6, 7],
	7: [11, 12, 13]
}))))

# def even_steven(cabinet: Dict[int, List[int]], num_bags_to_take: int) -> List[Dict[int, List[int]]]:
# 	return [
# 		{
# 			0: [1, 2],
# 			1: [2, 3]
# 		},
# 		{
# 			0: [1, 2, 3, 4]
# 		}
# 	]




# packings = set(str)
# for day in range(1, 4):
# 	next_day_packings = set(str)

# 	for packing in packings:
# 		cabinet: Dict[int, List[int]] = unpack(packing)

# 		# we just put it in with the rest
# 		cabinet[0].append(day)
# 		next_day_packings.add(pack(cabinet, 0))
# 		cabinet[0].pop()

# 		# we can grab an even number out the cabinet
# 		if len(cabinet[0]) >= 2:
# 			num_bags_to_take = 2
# 			while num_bags_to_take < len(cabinet[0]):
# 				for even_stevens_cabinet in even_steven(cabinet, num_bags_to_take):
# 					next_day_packings.add(pack(even_stevens_cabinet, 0))
# 				num_bags_to_take += 2

# 	packing = next_day_packings

# print(packing)
