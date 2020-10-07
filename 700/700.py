euler = 1504170715041707
mod   = 4503599627370517

M = mod % euler

v = 8912517754604
lowest = euler
for i in range(20000):
	nexxt = (v - M) % euler
	diff = nexxt - v
	v = (nexxt - euler) % diff
	# print('val, next, m, diff = ', v, nexxt, M, diff)
	if v < lowest:
		lowest = v
		print(v)

