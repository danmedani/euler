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


seq = generate_size_sequence(50, generate_starting_layer(5, 6, 19))
diff_seq = []
for i in range(len(seq) - 1):
	diff = seq[i+1] - seq[i]
	diff_seq.append(diff)
	# print(seq[i], diff)

for i in range(len(seq) - 2):
	print(seq[i], diff_seq[i], diff_seq[i + 1] - diff_seq[i])
# for x in range(10):
# 	for y in range(10):
# 		for z in range(10):
# 			e = encode(x, y, z)
# 			dx, dy, dz = decode(e)
# 			if x != dx or y != dy or z != dz:
# 				print('o no')