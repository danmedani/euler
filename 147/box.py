
def get_diamonds(a, b):
	diamonds = []
	val = a - 1
	for i in range(b - 1):
		diamonds.append(val)
		diamonds.append(val + 1)
	diamonds.append(val)
	return diamonds

def get_squares(diamonds):
	squares = []
	sum_vals_0 = diamonds[0]

	if len(diamonds) > 1:
		sum_vals_1 = diamonds[1]

	first_lane = []
	second_lane = []
	
	for x in range(sum_vals_0):
		first_lane.append((x, sum_vals_0 - x - 1))
	if len(diamonds) > 1:
		for x in range(sum_vals_1):
			second_lane.append((x, sum_vals_1 - x - 1))

	for box in first_lane:
		squares.append(box)
	for box in second_lane:
		squares.append(box)
	
	pairs_left = (len(diamonds) - 2) / 2
	for i in range(1, pairs_left + 1):
		for box in first_lane:
			squares.append((box[0] + i, box[1] + i))
		for box in second_lane:
			squares.append((box[0] + i, box[1] + i))

	for box in first_lane:
		squares.append((box[0] + pairs_left + 1, box[1] + pairs_left + 1))


	return squares

def get_shape(squares):
	level = 0
	shape = []
	while True:
		if len([
			square for square in squares
			if square[1] == level
		]) == 0:
			break
		min_x = min([
			square[0]
			for square in squares
			if square[1] == level
		])
		max_x = max([
			square[0]
			for square in squares
			if square[1] == level
		]) + 1

		shape.append((min_x, max_x))
		level = level + 1
	return shape

def count_rectangles_height(shape, rectangle_height):
	the_sum = 0
	for starting_y in range(len(shape) - rectangle_height + 1):
		starting_x = max([
			shape_row[0]
			for shape_row in shape[starting_y:starting_y+rectangle_height]
		])
		ending_x = min([
			shape_row[1]
			for shape_row in shape[starting_y:starting_y+rectangle_height]
		])
		room = ending_x - starting_x
		the_sum = the_sum + (
			(room * (room + 1)) / 2
		)
	return the_sum


def count_rectangles(shape):
	sum_rectangles = 0
	for rectangle_height in range(1, len(shape) + 1):
		sum_rectangles = sum_rectangles + count_rectangles_height(shape, rectangle_height)
	return sum_rectangles

def count_diags(a, b):
	diamonds = get_diamonds(a, b)
	squares = get_squares(diamonds)
	shape = get_shape(squares)
	return count_rectangles(shape)

def get_square_shape(a, b):
	shape = []
	for i in range(a):
		shape.append((0, b))
	return shape

def count_squares(a, b):
	return count_rectangles(
		get_square_shape(a, b)
	)

def total_count(a, b):
	return count_squares(a, b) + count_diags(a, b)

def count_all_smaller(x, y):
	summ = 0
	for a in range(1, x+1):
		for b in range(1, y+1):
			summ = summ + total_count(a, b)
	return summ

print(count_all_smaller(3, 2))
# print(total_count(3, 2))




