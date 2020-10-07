def process_triple(n: int, m: int, c: int):
	a = (m * m) - (n * n)
	b = 2 * m * n
	return (a, b, c * c)


def generate(max_c: int):
	n = 1
	m = 2
	while True:
		while True:
			v1 = (m * m) - (n * n)
			v2 = 2 * m * n
			
			a = min(v1, v2)
			b = max(v1, v2)
			c = (m * m) + (n * n)
			if c > max_c:
				if m == n + 1:
					return
				break

			yield process_triple(a, b, c)

			m += 2

		n += 1
		m = n + 1


count_not_super_perfect = 0
i = 0
for a, b, c in generate(1000):
	print(a, b, c)
	i += 1
	area = (a * b) / 2
	if not ((area % 6 == 0) and (area % 28 == 0)):
		count_not_super_perfect += 1
	

print(count_not_super_perfect)
print(i)
