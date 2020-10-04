from typing import Tuple
from typing import Set
from typing import List

POWER = 10000
SECOND_POWER = 100000000

def encode(cube: Tuple[int, int, int]) -> int:
	return cube[0] + (cube[1] * POWER) + (cube[2] * SECOND_POWER)

def decode(hashed_val: int) -> Tuple[int, int, int]:
	x = hashed_val % POWER
	y0 = (hashed_val - x) % SECOND_POWER
	y = int(y0 / POWER)
	z = int((hashed_val - y0) / SECOND_POWER)
	return (
		x,
		y,
		z
	)


def get_neighbors(cube: Tuple[int, int, int]) -> List[Tuple[int, int, int]]:
	return [
		(cube[0] - 1, cube[1], cube[2]),
		(cube[0] + 1, cube[1], cube[2]),
		(cube[0], cube[1] - 1, cube[2]),
		(cube[0], cube[1] + 1, cube[2]),
		(cube[0], cube[1], cube[2] - 1),
		(cube[0], cube[1], cube[2] + 1),
	]


def generate_size_sequence(num_steps: int, starting_layer: List[Tuple[int, int, int]]) -> List[int]:
	sequence: List[int] = []
	all_cubes = set()
	for cube in starting_layer:
		all_cubes.add(encode(cube))
	last_layer: List[Tuple[int, int, int]] = starting_layer

	for i in range(num_steps):
		this_layer: List[Tuple[int, int, int]] = []
		layer_count = 0
		for cube in last_layer:
			neighbors = get_neighbors(cube)
			for neighbor in neighbors:
				encoded_neighbor = encode(neighbor)
				if encoded_neighbor not in all_cubes:
					this_layer.append(neighbor)
					all_cubes.add(encoded_neighbor)
					layer_count += 1
		
		sequence.append(layer_count)
		last_layer = this_layer
	return sequence


def generate_starting_layer(x_size: int, y_size: int, z_size: int) -> List[Tuple[int, int, int]]:
	layer = []
	for x in range(x_size):
		for y in range(y_size):
			for z in range(z_size):
				layer.append((x, y, z))
	return layer

# seq = generate_size_sequence(10, generate_starting_layer(8, 8, 8))
# seq = generate_size_sequence(50, generate_starting_layer(2, 3, 1))

# print(seq[:5])
# diff_seq = []
# for i in range(len(seq) - 1):
# 	diff = seq[i+1] - seq[i]
# 	diff_seq.append(diff)
# 	# print(seq[i], diff)

# for i in range(len(seq) - 2):
# 	print(seq[i], diff_seq[i], diff_seq[i + 1] - diff_seq[i])


def gen_fast(x: int, y: int, z: int, max_num: int) -> List[int]:
	if min([x, y, z]) > 2:
		first = (x * y * z) - ((x - 2) * (y - 2) * (z - 2))
	else:
		first = x * y * z

	layer_length = 2 * ((x*y) + (x*z) + (y*z))
	delta = layer_length - first
	sequence = []
	while layer_length < max_num:
		sequence.append(layer_length)
		delta += 8
		layer_length += delta
	return sequence

print(gen_fast(11, 1, 1, 50))

# MAX = 1000
# MAX_DIM = 1000

# count_map = {}
# for x in range(1, MAX_DIM):
# 	for y in range(x, MAX_DIM):
# 		y_break = False
# 		for z in range(y, MAX_DIM):
# 			seq = gen_fast(x, y, z, MAX)
# 			if len(seq) > 0:
# 				for val in seq:
# 					if val not in count_map:
# 						count_map[val] = 0
# 					count_map[val] += 1
# 			else:
# 				if z > 1:
# 					# z too big - z is the cause. break out of z, go to next y
# 					break 
# 				else:
# 					# z not the problem. x or y are the problem
# 					if y > 1:
# 						# y too big. let's break out of z (and y!)
# 						y_break = True
# 						break
# 		if y_break:
# 			break



# ordered_keys = sorted(count_map.keys())

# for key in ordered_keys:
# 	print(key, count_map[key])





# for x in range(10):
# 	for y in range(10):
# 		for z in range(10):
# 			e = encode(x, y, z)






