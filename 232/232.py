from typing import Tuple
from functools import lru_cache
from fractions import Fraction

POSSIBLE_ZERO_POINTS = [0, 1]

T_RANGE = range(1, 9)
CHANCE_OF_ONE_POINTS = {
	t: Fraction(1, 2 ** t) for t in range(1, 9)
}
POSSIBLE_ONE_POINTS = {
	t: 2 ** (t - 1) for t in range(1, 9)
}

MIN_CHANCE_OF_BEING_HERE = Fraction(1, 10 ** 15)


@lru_cache(maxsize=150000)
def get_chance_of_1_winning(score: Tuple[int, int], zeros_turn: bool, chance_of_being_here: Fraction) -> Fraction:
	if chance_of_being_here < MIN_CHANCE_OF_BEING_HERE:
		return Fraction(0, 1)


	if score[1] >= 100 and score[0] >= 100:
		raise Exception('bad state both winners')


	if score[1] >= 100:
		return Fraction(1, 1)
	if score[0] >= 100:
		return Fraction(0, 1)

	if zeros_turn:
		return sum([
			Fraction(1, 2) * get_chance_of_1_winning((score[0] + zeros_points_this_turn, score[1]), not zeros_turn, chance_of_being_here * Fraction(1, 2))
			for zeros_points_this_turn in POSSIBLE_ZERO_POINTS
		])
	
	return max([
		CHANCE_OF_ONE_POINTS[t] * get_chance_of_1_winning((score[0], score[1] + POSSIBLE_ONE_POINTS[t]), not zeros_turn, chance_of_being_here * CHANCE_OF_ONE_POINTS[t])
		for t in T_RANGE
	])


print(get_chance_of_1_winning((0, 0), True, Fraction(1, 1)))
