import copy

hash_map = {}

def hash_digit_counts(val_so_far, digit_counts):
	return str(val_so_far) + '___' + '.'.join(
		str(dig) + '-' + str(digit_counts[dig])
		for dig in sorted(
			[
				digit for digit
				in digit_counts.keys()
			]
		)
	)


def sum_variations(
	digit_counts,
	val_so_far,
	mod
):
	# print('val_so_far = ', val_so_far)
	global hash_map
	if len(digit_counts.keys()) == 0:
		return val_so_far

	hash_val = hash_digit_counts(val_so_far, digit_counts)
	# print(hash_val)
	if hash_val in hash_map:
		return hash_map[hash_val]

	ssum = 0
	for digit in digit_counts.keys():
		digit_counts_copy = copy.deepcopy(digit_counts)
		if digit_counts_copy[digit] == 1:
			del digit_counts_copy[digit]
		else:
			digit_counts_copy[digit] -= 1

		ssum = ssum + (
			sum_variations(
				digit_counts_copy,
				(10 * val_so_far) + digit,
				mod
			)
		) % mod

	hash_map[hash_val] = ssum
	return ssum

def sum_variations_with_zeros(digit_counts, zero_count, mod):
	ssum = 0
	for digit in digit_counts.keys():
		# print('with zero count', zero_count, ', digit = ', digit)
		digit_counts_copy = copy.deepcopy(digit_counts)
		if digit_counts_copy[digit] == 1:
			del digit_counts_copy[digit]
		else:
			digit_counts_copy[digit] -= 1
		if zero_count > 0:
			digit_counts_copy[0] = zero_count
		# print(' digit_counts_copy', digit_counts_copy, ' digit = ', digit)
		variations = sum_variations(
			digit_counts_copy, 
			digit, 
			mod
		)
		# print('variations = ', variations)
		ssum = (
			ssum + (
				variations % mod
			)
		)
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


# def convert_pick_list_to_digit_counts(pick_list):
# 	digit_counts = []
# 	for key, val in pick_list.items():
# 		digit_counts.append(val)
# 	return digit_counts


def get_sum_for_val(
	val_to_reach, 
	total_digits_allowed,
	mod
):
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
	print(pick_list)
	total_sum = 0
	for pick in pick_list:
		# digit_counts = convert_pick_list_to_digit_counts(pick)
		print('pick', pick)
		total_digits = sum(
			[
				pick[digit]
				for digit in pick.keys()
			]
		)
		# print('total_digits', total_digits)

		for zero_count in range(total_digits_allowed - total_digits + 1):
			# print('zero_count', zero_count)
			sum_with_this_zero_count = sum_variations_with_zeros(
				pick, 
				zero_count,
				mod
			)
			# print('sum_with_this_zero_count', sum_with_this_zero_count)
			total_sum = (
				total_sum + sum_with_this_zero_count
			) % mod
			# print('total_sum', total_sum)
	return total_sum

# 9999..99 (19 9s) => 9*9 + 9*9 + ... + 9*9 = 1 539 -> max val = 39*39
squares = [
	a * a
	for a in range(1, 40)
]

ssum = 0
for square in squares:
	print('square', square)
	total_sum = get_sum_for_val(
		square,
		20,
		(10 ** 9)
	)
	ssum += total_sum
	print('total_sum', total_sum, ssum)
print(ssum)
# print(ssum + 1)

# 1111
# 2000
# 200
# 20
# 2


# remember to add 1 for 10 ** 20