#!/usr/bin/python

def isPan(d):
	dStr = str(d)
	for i in xrange(1, 10):
		if (str(i) not in dStr):
			return False
	return True

lenNum = 1

def setLen(num):
	global lenNum

	tenX = (10**lenNum)
	while (tenX % num == tenX):
		lenNum = lenNum + 1
		tenX = (10**lenNum)

a = 1
b = 1
i = 3

while True:
	num = a + b

	if (num > 10**10):
		if (isPan(num%(10**9))):
			print i, num%(10**9)
			setLen(num)
			big = 10**(lenNum - 9)
			first = (num-(num%(big))) / big
			if (isPan(first)):
				print 'pan', i, first, (num % (10 ** 9))
				break

	if (i % 2 == 0):
		a = num
	else:
		b = num

	i = i + 1


