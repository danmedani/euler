from typing import List
from functools import lru_cache

MOD = 10**25

def process_permutations(val: int) -> int:
	for
	return val


@lru_cache(maxsize=100000)
def mult(max_val: int, sum_to_reach: int, digits_left: int) -> List[int]:
	if sum_to_reach == 0:
		return [0]

	if digits_left <= 0:
		return []

	res = []
	for d in range(1, max_val + 1):
		mm = mult(max_val=d, sum_to_reach=sum_to_reach-d, digits_left=digits_left-1)
		for m in mm:
			res.append(m * 10 + d)

	return res


def get_all_combos():
	results = []
	for starting_digit in range(1, 10):
		for m in mult(max_val=starting_digit, sum_to_reach=starting_digit, digits_left=100):
			results += [m*10 + starting_digit]
	return results

combos = get_all_combos()
print(combos)

