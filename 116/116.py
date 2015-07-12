#!/usr/bin/python

def hashIt(tileLen, totalLen):
	return tileLen + ((10 ** 3)*totalLen)
mappy = {}

def getCount(tileLen, totalLen):
	v = hashIt(tileLen, totalLen)
	if (v in mappy):
		return mappy[v]

	if (tileLen == totalLen):
		mappy[v] = 1
		return 1
	if (tileLen > totalLen):
		mappy[v] = 0
		return 0
	
	r = totalLen-tileLen
	s = r + 1
	for i in xrange(0, r+1):
		c = getCount(tileLen, r-i)
		s = s + c

	mappy[v] = s
	return s

s = 0
for i in xrange(2, 5):
	s = s + getCount(i, 50)
	print s