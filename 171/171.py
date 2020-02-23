import copy

hash_map = {}

def hash_digit_counts(digit_counts):
	return '.'.join(str(digit) for digit in sorted(digit_counts))

def get_variations(digit_counts):
	global hash_map
	if len(digit_counts) <= 1:
		return 1

	hash_val = hash_digit_counts(digit_counts)
	if hash_val in hash_map:
		return hash_map[hash_val]

	ssum = 0
	for i in range(len(digit_counts)):
		digit_counts_copy = copy.deepcopy(digit_counts)
		if digit_counts_copy[i] == 1:
			digit_counts_copy.pop(i)
		else:
			digit_counts_copy[i] -= 1

		ssum += get_variations(digit_counts_copy)

	hash_map[hash_val] = ssum
	return ssum

def get_variations_with_zeros(digit_counts, zero_count):
	ssum = 0
	for i in range(len(digit_counts)):
		digit_counts_copy = copy.deepcopy(digit_counts)
		if digit_counts[i] == 1:
			digit_counts_copy.pop(i)
		else:
			digit_counts_copy[i] -= 1
		if zero_count > 0:
			digit_counts_copy.append(zero_count)
		# print(digit_counts_copy)
		ssum += get_variations(digit_counts_copy)
	return ssum

def ways_to_zero(val, max_option, picks_so_far, picks_left, pick_list):
	if val < 0:
		# too far bud
		return

	if val == 0:
		# we made it
		pick_list.append(picks_so_far)
		return

	if picks_left == 0:
		# we ran out of juice
		return

	for pick in range(1, max_option + 1):
		picks_so_far_copy = copy.deepcopy(picks_so_far)
		if pick in picks_so_far_copy:
			picks_so_far_copy[pick] += 1
		else:
			picks_so_far_copy[pick] = 1

		ways_to_zero(val - (pick * pick), pick, picks_so_far_copy, picks_left - 1, pick_list)


def convert_pick_list_to_digit_counts(pick_list):
	digit_counts = []
	for key, val in pick_list.items():
		digit_counts.append(val)
	return digit_counts


def get_total_counts(val_to_reach, total_digits_allowed):
	pick_list = []
	print('ways to zero, go')
	ways_to_zero(
		val_to_reach,
		9,
		{},
		total_digits_allowed,
		pick_list
	)
	print('pick count, go')
	total_counts = 0
	for pick in pick_list:
		digit_counts = convert_pick_list_to_digit_counts(pick)
		total_digits = sum(digit_counts)

		for zero_count in range(total_digits_allowed - total_digits + 1):
			total_counts = total_counts + get_variations_with_zeros(
				digit_counts, 
				zero_count
			)
	return total_counts

# 9999..99 (19 9s) => 9*9 + 9*9 + ... + 9*9 = 1 539 -> max val = 39*39
squares = [
	a * a
	for a in range(1, 40)
]

ssum = 0
for square in squares:
	print('square', square)
	total_counts = get_total_counts(
		square,
		20
	)
	ssum += total_counts
	print('total_counts', total_counts, ssum)
print(ssum)
print(ssum + 1)

# remember to add 1 for 10 ** 20