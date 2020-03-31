from fractions import Fraction

exact_shots_to_make = 20
num_total_shots = 50
hash_table = {}

def hash_it(shot_number: int, shots_made: int) -> str:
	return ((1 + shot_number) * 100) + (1 + shots_made)

def calc_probability_making_exactly(
	shot_number: int,
	shots_made: int,
	q: Fraction
):
	global hash_table, exact_shots_to_make, num_total_shots

	hash_val = hash_it(shot_number, shots_made)
	if hash_val in hash_table:
		return hash_table[hash_val]

	shots_left = num_total_shots - shot_number + 1
	if shots_left + shots_made < exact_shots_to_make:
		return Fraction(0, 1)

	if shots_made > exact_shots_to_make:
		return Fraction(0, 1)

	if shots_left == 0 and shots_made == exact_shots_to_make:
		return Fraction(1, 1)

	prob_if_make = (Fraction(1, 1) - (Fraction(shot_number, q))) * calc_probability_making_exactly(
		shot_number + 1,
		shots_made + 1,
		q
	)
	prob_if_miss = (Fraction(1, 1) * Fraction(shot_number, q)) * calc_probability_making_exactly(
		shot_number + 1,
		shots_made,
		q
	)
	total_prob_from_here = prob_if_make + prob_if_miss

	hash_table[hash_val] = total_prob_from_here

	return total_prob_from_here


def calc_making_it(q):
	global hash_table
	hash_table = {}
	return calc_probability_making_exactly(1, 0, q)


val = Fraction(50, 1)
for place in range(0, 20):
	while calc_making_it(val) >= Fraction(2, 100):
		if calc_making_it(val) == Fraction(2, 100):
			print('holy shiitttt')

		val = val + Fraction(1, 10 ** place)
		
	val = val - Fraction(1, 10 ** place)
	print(val, val.numerator / val.denominator)
