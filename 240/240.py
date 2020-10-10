import math
from functools import lru_cache


@lru_cache(maxsize=10000)
def count_ways(
	top_dice_left: int, 
	ceiling: int, 
	sum_left: int, 
	dice_sides: int, 
	other_dice_count: int
) -> int:
	if top_dice_left == 0:
		assert sum_left == 0
		return ceiling ** other_dice_count

	new_ceiling = min(ceiling, sum_left)
	new_floor = max(math.ceil(sum_left / top_dice_left), 1)

	if new_floor > new_ceiling:
		return 0

	return sum([
		count_ways(
			top_dice_left=top_dice_left - 1,
			ceiling=roll,
			sum_left=sum_left - roll,
			dice_sides=dice_sides,
			other_dice_count=other_dice_count
		)
		for roll in range(new_floor, new_ceiling + 1)
	])


print(
	count_ways(
		top_dice_left=3,
		ceiling=6,
		sum_left=15,
		dice_sides=6,
		other_dice_count=2
	)
)
