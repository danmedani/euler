#!/usr/bin/python
import copy, random

MAX = 10 ** 5
a = 1
b = 50
mappy = {}

def hashIt(numberBag, exponent):
	return reduce(lambda x, y : x + '|' +  y, map(str, sorted(numberBag))) + str(exponent)

lowBall = MAX
def iterate(numberBag, exponent):
	global lowBall

	hVal = hashIt(numberBag, exponent)
	if (hVal in mappy):
		return mappy[hVal]

	numMults = len(numberBag) - 1

	if (numMults > lowBall):
		return MAX

	if (exponent in numberBag):
		# o, we found it
		if (numMults < lowBall):
			lowBall = numMults
		return numMults

	# gather all possible branches
	branches = []
	newVals = set()
	for a in numberBag:
		for b in numberBag:
			v = a + b
			# haven't seen # and it's < exponent
			# better way to trim?
			if ((v not in numberBag) and (v not in newVals) and (v <= exponent)):
				branches.append(v)
				newVals.add(v)

	# find min for each branch
	minimum = MAX
	for branch in reversed(sorted(branches)):
		newNumberBag = copy.deepcopy(numberBag)
		newNumberBag.add(branch)
		minVal = iterate(newNumberBag, exponent)
		if minVal < minimum:
			minimum = minVal

	mappy[hVal] = minimum
	if (minimum < lowBall):
		lowBall = minimum
	return minimum

def getMinMult(n):
	global lowBall, mappy

	mappy = {}
	lowBall = MAX
	return iterate(set([1]), n)

def getSumMinMult(a, b):
	s = 0
	for i in xrange(a, b):
		minMult = getMinMult(i)
		s = s + minMult

		print 'i', i, '\tmin(i)', minMult
	
	return s


getSumMinMult(a, b)


