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


def generate_size_sequence(max_num: int, starting_layer: List[Tuple[int, int, int]]) -> List[int]:
	sequence: List[int] = []
	all_cubes = set()
	for cube in starting_layer:
		all_cubes.add(encode(cube))
	last_layer: List[Tuple[int, int, int]] = starting_layer


	while len(last_layer) < max_num:
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



def generate_size_sequence_with_steps(max_steps: int, starting_layer: List[Tuple[int, int, int]]) -> List[int]:
	sequence: List[int] = []
	all_cubes = set()
	for cube in starting_layer:
		all_cubes.add(encode(cube))
	last_layer: List[Tuple[int, int, int]] = starting_layer


	for i in range(max_steps):
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


def gen_slow(x: int, y: int, z: int, max_num: int) -> List[int]:
	return generate_size_sequence(max_num, generate_starting_layer(x, y, z))[:-1]

def gen_fast(x: int, y: int, z: int, max_num: int) -> List[int]:
	# if x > 2:
	# 	first = (x * y * z) - ((x - 2) * (y - 2) * (z - 2))
	# else:
	# 	# if x == 1:
	# 	# 	seq = generate_size_sequence_with_steps(2, generate_starting_layer(x, y, z))
	# 	# 	first = seq[0] - (seq[1] - seq[0] - 8)
	# 	# else:
	# 	first = x * y * z

	layer_length = 2 * ((x*y) + (x*z) + (y*z))
	second_layer_length = layer_length + (4 * (x + y + z))
	delta = second_layer_length - layer_length - 8
	
	sequence = []
	while layer_length < max_num:
		sequence.append(layer_length)
		delta += 8
		layer_length += delta
	return sequence

# print(gen_slow(6, 12, 14, 2000))
# print(gen_fast(6, 12, 14, 2000))

MAX = 20000
MAX_DIM = MAX

count_map = {}
for x in range(1, MAX_DIM):
	print(x)
	for y in range(x, MAX_DIM):
		y_break = False
		for z in range(y, MAX_DIM):
			# if gen_slow(x, y, z, MAX) != gen_fast(x, y, z, MAX):
			# 	print('o nooooo', x, y, z)
			# 	print(gen_slow(x, y, z, MAX))
			# 	print(gen_fast(x, y, z, MAX))
			# 	print()


			seq = gen_fast(x, y, z, MAX)
			if len(seq) > 0:
				for val in seq:
					if val not in count_map:
						count_map[val] = 0
					count_map[val] += 1

			else:
				if z > 1:
					# z too big - z is the cause. break out of z, go to next y
					break 
				else:
					# z not the problem. x or y are the problem
					if y > 1:
						# y too big. let's break out of z (and y!)
						y_break = True
						break
		if y_break:
			break

print('hi')

ordered_keys = sorted(count_map.keys())

for key in ordered_keys:
	if count_map[key] == 1000:
		print('found one', key, count_map[key])
	# print(key, count_map[key])





# for x in range(10):
# 	for y in range(10):
# 		for z in range(10):
# 			e = encode(x, y, z)






