import math
from functools import reduce

def prod(l):
	return reduce(lambda x, y: x * y, l)

def list_for_num(num):
	return [(1.0 * (i * 2) / (num + 1)) ** i for i in range(1, num+1)]

print(
	sum(
		[
			math.floor(
				prod(
					list_for_num(x)
				)
			)
			for x in range(2, 16)
		]
	)
)
