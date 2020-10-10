from math import comb
from fractions import Fraction
from functools import lru_cache

# P: Prime in place
# O: Prime out of place
# X: Doesn't matter
# 1 2 3 4 5 6 ... 24 25 26 27 ... 100
# P P P O O O ...  O  O  X  X ...   X

# choose 3 primes from the 25
chance = Fraction(comb(25,3), 1)

# choose the first 3 primes correctly
chance = chance * Fraction(1, 100) * Fraction(1, 99) * Fraction(1, 98)

@lru_cache(maxsize=10000)
def find_chance(prime_count: int, other_count: int, prime_spots_left: int, other_spots_left: int) -> Fraction:
	if prime_count < 0 or other_count < 0:
		return 0

	if prime_spots_left == 0:
		return 1 

	total_spots_left = prime_spots_left + other_spots_left
	return (

		# choose one of the other primes (not the right one, though)
		Fraction(prime_count - 1, total_spots_left) * find_chance( 
			prime_count=prime_count - 2, # prime we use goes, prime that should have gone here goes
			other_count=other_count + 1, # prime that should have gone here is newly other
			prime_spots_left=prime_spots_left - 2, # we advance 1 position, and lose the spot of the prime we used
			other_spots_left=other_spots_left + 1  # spot of prime we used now an 'other'
		)
	) + (

		# choose one of the randos
		Fraction(other_spots_left, total_spots_left) * find_chance(
			prime_count=prime_count - 1, # prime that should have gone here goes
			other_count=other_count, # 
			prime_spots_left=prime_spots_left - 1, # advance 1 position
			other_spots_left=other_spots_left
		)
	)

chance = chance * find_chance(prime_count=22, other_count=75, prime_spots_left=22, other_spots_left=75)
print(chance)

