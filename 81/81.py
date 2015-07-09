#!/usr/bin/python

f = open('p081_matrix.txt', 'r')

hashy = {}

mat = []
for line in f:
	l = line[0:len(line)-1]
	mat.append(map(int, l.split(',')))

def hashIt(x, y):
	return (x * 1000) + y

def findSho(x, y):
	hashVal = hashIt(x, y)
	if (hashVal in hashy):
		return hashy[hashVal]

	ret = mat[x][y]
	if (x == 79 and y < 79):
		ret = ret + findSho(x, y+1)
	elif (x < 79 and y == 79):
		ret = ret + findSho(x+1, y)
	elif (x < 79 and y < 79):
		retDown = findSho(x+1, y)
		retRight = findSho(x, y+1)
		ret = ret + min(retDown, retRight)

	hashy[hashVal] = ret
	return ret

print findSho(0, 0)