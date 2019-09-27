from functools import lru_cache


@lru_cache(maxsize=100000)
def gen_nums(num_digits):
	if num_digits == 0:
		return list(range(1, 3))

	nums = []
	other_nums = gen_nums(num_digits - 1)
	
	for other in other_nums:
		other_mult = other * 10
		for i in range(3):
			nums.append(other_mult + i)
	return nums

interesting_multiples = []
for i in range(15):
	for num in gen_nums(i):
		interesting_multiples.append(num)

print(len(interesting_multiples))
interesting_multiples.sort()
print('sorted')

seen_nat = set()
nat_nums = range(10001)
not_seen = set(nat_nums)
nat_set = set(nat_nums)

big_sum = 0
print(interesting_multiples[0])
for twoonezero in interesting_multiples:
	for nat in list(not_seen):
		if nat not in seen_nat:
			if twoonezero < nat:
				break

			if twoonezero % nat == 0:
				big_sum += int(twoonezero / nat)
				seen_nat.add(nat)
				not_seen.remove(nat)


print(big_sum)
print(len(not_seen))
print(not_seen)