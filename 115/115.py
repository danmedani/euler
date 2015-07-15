#!/usr/bin/python

def hashIt(totalLen, onBlack):
	return (-1 if onBlack else 1) * totalLen
mappy = {}

def getCount(minBlock, totalLen, onBlack):
	# print totalLen, onBlack
	v = hashIt(totalLen, onBlack)
	if (v in mappy):
		return mappy[v]

	if (totalLen == 0):
		mappy[v] = 1
		return 1
	if (totalLen < 0):
		return 0
	
	s = 0
	s = s + getCount(minBlock, totalLen-1, True)
	if (onBlack):
		bLen = minBlock
		while (totalLen - bLen >= 0):
			s = s + getCount(minBlock, totalLen - bLen, False)
			bLen = bLen + 1

	mappy[v] = s
	return s


for i in xrange(2, 100000000):
	if (getCount(50, i, True) > (10**6)):
		print i, getCount(50, i, True), getCount(50, i-1, True)
		break

