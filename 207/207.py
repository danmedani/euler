from fractions import Fraction

def get_k(x):
	return 4 ** x - 2 ** x

def get_t(x):
	return (x+1) ** 2 - (x+1)

limit = Fraction(1, 12345)

index_k = 1
index_t = 1

while Fraction(index_k, index_t) >= limit:
	print(index_k, get_k(index_k), '__', index_t, get_t(index_t))

	index_t += 1
	if get_t(index_t) >= get_k(index_k+1):
		index_k += 1


print()
print(index_k, get_k(index_k), '__', index_t, get_t(index_t))

