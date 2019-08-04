from functools import lru_cache

@lru_cache(maxsize=10000)
def get_count(digits_left, gone_up, space_on_left, space_on_right):
	if digits_left == 0:
		return 1 if gone_up else 0

	total_count = 0
	if not gone_up and space_on_right > 0:
		# print(spacey, 'going right')
		for new_space_added_to_left in range(space_on_right):
			total_count += get_count(
				digits_left=digits_left - 1, 
				gone_up=True, 
				space_on_left=space_on_left + new_space_added_to_left, 
				space_on_right=None
			)

	for new_space_left in range(0, space_on_left):
		total_count += get_count(
			digits_left=digits_left - 1, 
			gone_up=gone_up, 
			space_on_left=new_space_left, 
			space_on_right=None if gone_up else space_on_right + (space_on_left - new_space_left - 1)
		)

	return total_count


def get_count_size(size):
	return sum([
		get_count(
			digits_left=size - 1, 
			gone_up=False, 
			space_on_left=space_on_left, 
			space_on_right=25 - space_on_left
		) for space_on_left in range(0, 26)
	])

maxx = -1
for i in range(1, 27):
	cs = get_count_size(i)
	print(i, cs)
	if cs > maxx:
		maxx = cs
print(maxx)

