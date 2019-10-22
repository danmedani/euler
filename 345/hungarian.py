from random import randint

old_mat = [
	[7,53,183,439,863,497,383,563,79,973,287,63,343,169,583],
	[627,343,773,959,943,767,473,103,699,303,957,703,583,639,913],
	[447,283,463,29,23,487,463,993,119,883,327,493,423,159,743],
	[217,623,3,399,853,407,103,983,89,463,290,516,212,462,350],
	[960,376,682,962,300,780,486,502,912,800,250,346,172,812,350],
	[870,456,192,162,593,473,915,45,989,873,823,965,425,329,803],
	[973,965,905,919,133,673,665,235,509,613,673,815,165,992,326],
	[322,148,972,962,286,255,941,541,265,323,925,281,601,95,973],
	[445,721,11,525,473,65,511,164,138,672,18,428,154,448,848],
	[414,456,310,312,798,104,566,520,302,248,694,976,430,392,198],
	[184,829,373,181,631,101,969,613,840,740,778,458,284,760,390],
	[821,461,843,513,17,901,711,993,293,157,274,94,192,156,574],
	[34,124,4,878,450,476,712,914,838,669,875,299,823,329,699],
	[815,559,813,459,522,788,168,586,966,232,308,833,251,631,107],
	[813,883,451,509,615,77,281,613,459,205,380,274,302,35,805]
]
# mat = [
# 	[108, 125, 150],
# 	[150, 135, 175],
# 	[122, 148, 250]
# ]

mat = []
for row_index in range(len(old_mat)):
	new_row = []
	for col_index in range(len(old_mat)):
		new_row.append(1000 - old_mat[row_index][col_index])
	mat.append(new_row)


def step_one(mat):
	for row_index in range(len(mat)):
		smallest_val_in_row = min(mat[row_index])
		for col_index in range(len(mat)):
			mat[row_index][col_index] = mat[row_index][col_index] - smallest_val_in_row

def step_two(mat):
	for col_index in range(len(mat)):
		col = [row[col_index] for row in mat]
		smallest_val_in_col = min(col)
		for row_index in range(len(mat)):
			mat[row_index][col_index] = mat[row_index][col_index] - smallest_val_in_col

def get_max_rows(mat, row_covers, col_covers):
	max_num_zeros = 0
	max_row = -1
	for row_index in range(len(mat)):
		if row_index not in row_covers:
			count_zeros_in_this_row = 0
			for col_index in range(len(mat)):
				if col_index not in col_covers and mat[row_index][col_index] == 0:
					count_zeros_in_this_row += 1

			if count_zeros_in_this_row > max_num_zeros:
				max_num_zeros = count_zeros_in_this_row
				max_row = row_index
	return max_row, max_num_zeros

def get_max_cols(mat, row_covers, col_covers):
	max_num_zeros = 0
	max_col = -1
	for col_index in range(len(mat)):
		if col_index not in col_covers:
			count_zeros_in_this_col = 0
			for row_index in range(len(mat)):
				if row_index not in row_covers and mat[row_index][col_index] == 0:
					count_zeros_in_this_col += 1

			if count_zeros_in_this_col > max_num_zeros:
				max_num_zeros = count_zeros_in_this_col
				max_col = col_index

	return max_col, max_num_zeros

def uncovered_zero_count(mat, row_covers, col_covers):
	zero_count = 0
	for row_index in range(len(mat)):
		for col_index in range(len(mat)):
			if row_index not in row_covers and col_index not in col_covers and mat[row_index][col_index] == 0:
				zero_count += 1
	return zero_count

def print_mat(mat):
	for row in mat:
		line = ''
		for val in row:
			line = line + (str(val) + ' ').ljust(4) 
		print(line)
	print('')

def cover(mat, row_covers, col_covers):
	while uncovered_zero_count(mat, row_covers, col_covers) > 0:
		max_row, max_row_zeros = get_max_rows(mat, row_covers, col_covers)
		max_col, max_col_zeros = get_max_cols(mat, row_covers, col_covers)

		if max_row_zeros > max_col_zeros:
			row_covers.add(max_row)
		elif max_row_zeros < max_col_zeros:
			col_covers.add(max_col)
		else:
			if randint(0,1) == 0:
				row_covers.add(max_row)
			else:
				col_covers.add(max_col)


def smallest_uncovered(mat, row_covers, col_covers):
	smallest = 10**9
	for row_index in range(len(mat)):
		for col_index in range(len(mat)):
			if row_index not in row_covers and col_index not in col_covers:
				if mat[row_index][col_index] < smallest:
					smallest = mat[row_index][col_index]
	return smallest

def sub_val(mat, row_covers, col_covers, sub_val):
	for row_index in range(len(mat)):
		if row_index not in row_covers:
			for col_index in range(len(mat)):
				mat[row_index][col_index] -= sub_val

	for col_index in range(len(mat)):
		if col_index in col_covers:
			for row_index in range(len(mat)):
				mat[row_index][col_index] += sub_val
	


# print_mat(mat)
# print()
step_one(mat)
# print_mat(mat)
# print()
step_two(mat)
# print_mat(mat)
# print()

row_covers = set([])
col_covers = set([])

while len(row_covers) + len(col_covers) < len(mat):
	row_covers = set([])
	col_covers = set([])

	cover(mat, row_covers, col_covers)
	# print(row_covers, col_covers)

	sub_val(mat, row_covers, col_covers, smallest_uncovered(mat, row_covers, col_covers))
	
print('row_covers', row_covers)
print('col_covers', col_covers)
print()

print_mat(mat)

row_options = {i: set() for i in range(len(mat))}
for row_index in range(len(mat)):
	for col_index in range(len(mat)):
		if mat[row_index][col_index] == 0:
			row_options[row_index].add(col_index)

for i in range(len(mat)):
	print(i, row_options[i])

row_map = {i: None for i in range(len(mat))}
for i in range(len(mat)):
	if len(row_options[i]) == 1:
		only_option = row_options[i].pop()
		row_map[i] = only_option
		
		for j in range(len(mat)):
			if only_option in row_options[j] and i != j:
				row_options[j].remove(only_option)
print()
for i in range(len(mat)):
	print(i, row_map[i])

print()
for i in range(len(mat)):
	if not row_map[i]:
		print(i, row_options[i])



