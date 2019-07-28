
max_prod = 0

def get_best(total, exponent, sections):
	if exponent == 1:
		return total

	best_so_far = -1
	my_best_so_far = -1

	section_size = total / sections

	for i in range(1, sections):
		my_amount = i * section_size
 
		total_size = (my_amount ** exponent) * \
			get_best(total - my_amount, exponent - 1, sections)
		
		if total_size > best_so_far:
			best_so_far = total_size
			my_best_so_far = my_amount

	return best_so_far

vals = []

buckets = 10
sections = 5
print(get_best(buckets, buckets, sections))

