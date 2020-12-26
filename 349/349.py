from typing import NamedTuple

black_grid = set()

def print_grid():
	min_x = 10 ** 10
	max_x = -1 * 10 ** 10
	min_y = 10 ** 10
	max_y = -1 * 10 ** 10
	for black_hash in black_grid:
		x, y = black_hash.split('|')
		x_int = int(x)
		y_int = int(y)

		if x_int < min_x:
			min_x = x_int
		if x_int > max_x:
			max_x = x_int
		if y_int < min_y:
			min_y = y_int
		if y_int > max_y:
			max_y = y_int
	
	for y in range(max_y, min_y - 1, -1):
		row = []
		for x in range(min_x, max_x + 1):
			if hash(x, y) in black_grid:
				row.append('X')
			else:
				row.append(' ')
		print(row)




def hash(x: int, y: int) -> str:
	# return (x * 100000) + y
	return str(x) + '|-|' + str(y)

def get_dir_turn_counter_clock(direction: str) -> str:
	if direction == 'W':
		return 'S'
	if direction == 'S':
		return 'E'
	if direction == 'E':
		return 'N'
	if direction == 'N':
		return 'W'

def get_dir_turn_clock(direction: str) -> str:
	if direction == 'W':
		return 'N'
	if direction == 'N':
		return 'E'
	if direction == 'E':
		return 'S'
	if direction == 'S':
		return 'W'

def move_forward(x: int, y: int, direction: str):
	if direction == 'N':
		return (x, y + 1)
	if direction == 'S':
		return (x, y - 1)
	if direction == 'W':
		return (x - 1, y)
	if direction == 'E':
		return (x + 1, y)


x_pos = 100
y_pos = -10
direction = 'N'
for step in range(1, 1000000):
	pos_hash = hash(x_pos, y_pos)
	if pos_hash in black_grid:
		black_grid.remove(pos_hash) # turn it white
		direction = get_dir_turn_counter_clock(direction)
	else:
		black_grid.add(pos_hash)
		direction = get_dir_turn_clock(direction)
	x_pos, y_pos = move_forward(x_pos, y_pos, direction)

	if step > 997000:
		print(str(step) + '\t' + str(len(black_grid)))



# print_grid()
# print('--', len(black_grid))
# print()
	# print(i, len(black_grid))
	# print(x_pos, y_pos)


# print(len(black_grid))