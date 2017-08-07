def hash(dig, steps, min_cov, max_cov):
	return dig + ((1+steps) * 150) + ((1+min_cov) * 10000) + ((1+max_cov) * 10000000)

def num_ways(dig, steps, min_cov, max_cov, total_len, h_map):
	h_val = hash(dig, steps, min_cov, max_cov)
	if h_val in h_map:
		return h_map[h_val]

	ans = 0
	if steps == total_len:
		if min_cov == 0 and max_cov == 9:
			ans = 1
		else:
			ans = 0
	else:
		if dig == 9:
			ans = num_ways(8, steps + 1, min(8, min_cov), max_cov, total_len, h_map)
		elif dig == 0:
			ans = num_ways(1, steps + 1, min_cov, max(1, max_cov), total_len, h_map)
		else:
			ans = num_ways(dig - 1, steps + 1, min(dig - 1, min_cov), max_cov, total_len, h_map) + num_ways(dig + 1, steps + 1, min_cov, max(max_cov, dig + 1), total_len, h_map)

	h_map[h_val] = ans
	return ans

s = 0
for num_len in xrange(9, 40):
	h_map = {}
	for start_val in xrange(1, 10):
		s = s + num_ways(start_val, 0, start_val, start_val, num_len, h_map)

print s
