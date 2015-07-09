#!/usr/bin/python

mappy = {}

def hashy(n, midway):
	return n + (midway * 1000)

def countLeaves(n, midway):
	hVal = hashy(n, midway)
	if (hVal in mappy):
		return mappy[hVal]

	if (n == midway):
		return 1

	newMids = midway - n
	maxxy = min(newMids, n)
	
	ss = 0
	for i in xrange(1, maxxy+1):
		ss = ss + countLeaves(i, newMids)

	mappy[hVal] = ss
	return ss

def getSumzy(num):
	sumzy = 0
	for i in xrange(1, num+1):
		tt = countLeaves(i, num)
		# print i, tt
		sumzy = sumzy + tt

	return sumzy

n = 5
sz = getSumzy(n)
while (sz % 1000000 != 0):
	n = n + 1
	sz = getSumzy(n)
	print n, sz

