#!/usr/bin/python
import math

hashMap = {}

def prime(n):
	if (n == 2):
		return True
	for i in xrange(2, int(math.ceil(math.sqrt(n)))+1):
		if (n % i == 0):
			return False
	return True

pList = []
for i in xrange(2, 1000000):
	if (prime(i)):
		pList.append(i)

cnt = 0
i = 0
j = 0
k = 0
while pList[i] < 7071:
	j = 0
	while pList[j] < 368:
		k = 0
		while pList[k] < 84:
			val = (pList[i] ** 2) + (pList[j] ** 3) + (pList[k] ** 4)
			if val < 50000000:
				if not val in hashMap:
					print val, i, j, k, cnt
					hashMap[val] = True
					cnt = cnt + 1
			k = k + 1
		j = j + 1
	i = i + 1

print cnt
