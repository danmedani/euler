#!/usr/bin/python

def hashIt(totalLen):
	return totalLen
mappy = {}

def getCount(blocks, totalLen):
	v = hashIt(totalLen)
	if (v in mappy):
		return mappy[v]

	if (totalLen == 0):
		mappy[v] = 1
		return 1
	if (totalLen < 0):
		return 0
	
	s = 0
	for i in xrange(0, len(blocks)):
		s = s + getCount(blocks, totalLen - blocks[i])

	mappy[v] = s
	return s

print getCount([1, 2, 3, 4], 50)