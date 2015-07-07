#!/usr/bin/python
import math

def parse(line):
	line = line[:-1]
	nums = line.split(',')
	triSet = [
		{'x': int(nums[0]), 'y': int(nums[1])},
		{'x': int(nums[2]), 'y': int(nums[3])},
		{'x': int(nums[4]), 'y': int(nums[5])}
	]

	return triSet

f = open('p102_triangles.txt')
triz = []
line = f.readline()
while (len(line) > 0):
	triz.append(parse(line))
	line = f.readline()

def getArea(a, b, c):
	return abs(1.0*((a['x'] * (b['y'] - c['y'])) + (b['x'] * (c['y'] - a['y'])) + (c['x'] * (a['y'] - b['y']))) / 2)

s = 0
for i in xrange(len(triz)):
	areaTri = getArea(triz[i][0], triz[i][1], triz[i][2])
	area1 = getArea(triz[i][0], triz[i][1], {'x': 0, 'y': 0})
	area2 = getArea(triz[i][0], {'x': 0, 'y': 0}, triz[i][2])
	area3 = getArea({'x': 0, 'y': 0}, triz[i][1], triz[i][2])
	if (abs(area1 + area2 + area3 - areaTri) < 0.001):
		s = s + 1

print s