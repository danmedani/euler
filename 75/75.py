#!/usr/bin/python
import math
c = 0
def square(n):
	global c
	c = c + 1
	sqN = int(math.sqrt(n))
	return (sqN ** 2 == n)

def genMapKey(a, b, c):
	oList = sorted([a, b, c])
	return str(oList[0]) + '|' + str(oList[1]) + '|' + str(oList[2])

def getCount(x):
	seenMap = {}
	s = 0
	counter = [0]*(x+1)
	for n in xrange(1, x):
		for m in xrange(n+1, x):
			a = (m**2) - (n**2)
			b = 2 * m * n
			c = (m**2) + (n**2)

			total = a + b + c
			if (total > x):
				break

			key = genMapKey(a, b, c)
			if (key not in seenMap):
				seenMap[key] = True
				counter[total] = counter[total] + 1
				
				if (counter[total] == 1):
					s = s + 1
				elif (counter[total] == 2):
					s = s - 1
						
				for i in xrange(2, x):
					aN = a * i
					bN = b * i
					cN = c * i

					total = aN + bN + cN
					if (total > x):
						break

					key = genMapKey(aN, bN, cN)
					if (key not in seenMap):
						seenMap[key] = True
						counter[total] = counter[total] + 1
						if (counter[total] == 1):
							s = s + 1
						elif (counter[total] == 2):
							s = s - 1

				

	return s

print getCount(1500000)