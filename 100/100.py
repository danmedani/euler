#!/usr/bin/python

p = 3
q = 2
k = 0
r = 4
s = 3
l = -1

x = 1
y = 0

while (y < 10**12):
	x0 = x
	x = (p * x) + (q * y) + k
	y = (r * x0) + (s * y) + l
	print x, y