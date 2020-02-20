
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
	sum_vals_1 = diamonds[1]

	first_lane = []
	second_lane = []
	
	for x in range(sum_vals_0):
		first_lane.append((x, sum_vals_0 - x - 1))
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

diamonds = get_diamonds(4, 3)
print(diamonds)
print(get_squares(diamonds))



