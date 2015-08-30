#!/usr/bin/python
import copy

MAX = 10 ** 5
a = 1
b = 25
mappy = {}

def hashIt(numberBag, exponent):
	return reduce(lambda x, y : x + '|' +  y, map(str, sorted(numberBag))) + str(exponent)

def iterate(numberBag, exponent):
	hVal = hashIt(numberBag, exponent)
	if (hVal in mappy):
		return mappy[hVal]

	if (exponent in numberBag):
		# o, we found it
		return len(numberBag) - 1

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
	for branch in branches:
		newNumberBag = copy.deepcopy(numberBag)
		newNumberBag.add(branch)
		minVal = iterate(newNumberBag, exponent)
		if minVal < minimum:
			minimum = minVal

	mappy[hVal] = minimum
	return minimum

def getMinMult(n):
	mappy = {}
	return iterate(set([1]), n)

def getSumMinMult(a, b):
	s = 0
	for i in xrange(a, b):
		minMult = getMinMult(i)
		s = s + minMult

		print 'i', i, '\tmin(i)', minMult
	
	return s


getSumMinMult(a, b)


