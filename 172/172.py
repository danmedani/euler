from functools import lru_cache

@lru_cache(maxsize=10000)
def get_times(bucket_zero, bucket_one, bucket_two, depth, max_depth):
	if depth == max_depth:
		return 1

	times = 0
	if bucket_zero > 0:
		times += bucket_zero * get_times(bucket_zero-1, bucket_one+1, bucket_two, depth+1, max_depth)
	if bucket_one > 0:
		times += bucket_one * get_times(bucket_zero, bucket_one-1, bucket_two+1, depth+1, max_depth)
	if bucket_two > 0:
		times += bucket_two * get_times(bucket_zero, bucket_one, bucket_two-1, depth+1, max_depth)
	return times

def get_number_ways(digits):
	return 9 * get_times(9, 1, 0, 1, digits)


print(
	get_number_ways(18)
)


# 227,485,267,000,992,000
# 227485267000992000
