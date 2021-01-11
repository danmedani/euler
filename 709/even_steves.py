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
		packing.append(str(a_bag))
		if a_bag in cabinet:
			packing.append('(')
			packing.append(pack(a_bag, cabinet))
			packing.append(')')
	return ''.join(packing)

print(pack(0, {
	0: [1, 2, 3],
	1: [4, 5],
	5: [6, 7]	
}))

# def unpack(packing: str) -> Dict[int, List[int]]:
# 	cabinet = {}
# 	current_bag = 0
# 	bag_stack = []
# 	for index in range(len(packing)):
# 		if packing[index] not in ['(', ')']:
# 			cabinet[current_bag].append(int(packing[index]))
# 		elif packing[index] == '(':
# 			bag_stack.append(current_bag)
# 			current_bag = packing[index]
			





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
