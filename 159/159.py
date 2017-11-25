# List of factors (1 ... x)
def getFactors(x):
	factors = []
	for i in xrange(x):
		factors.append([])

	for i in xrange(2, x):
		j = i
		while j < x:
			factors[j].append(i)
			j = j + i

	return factors

def hashList(list):
	hVal = ''
	sList = sorted(list)
	for val in sList:
		hVal = hVal + str(val) + '-'
	return hVal

# Given list of factors of a number, get all factorizations of it.
def getFax(number, dividers, pastFax):
	hashed = {}
	fax = [[number]]
	for div in dividers:
		if div != number:
			d1 = pastFax[div]
			d2 = pastFax[number / div]
			for v1 in d1:
				for v2 in d2:
					combo = v1 + v2
					hList = hashList(combo)
					if hList not in hashed:
						hashed[hList] = True
						fax.append(v1 + v2)
	return fax

# Sum of the digits in a number
def sumDigits(number):
	ssum = 0
	while number > 0:
		ssum = ssum + (number % 10)
		number = number / 10
		if ssum >= 10:
			ssum = sumDigits(ssum)
	return ssum

# Sum of the sumDigits of a set of numbers
def drs(fax):
	return sum([sumDigits(f) for f in fax])

# Max digital root sum!
def mdrs(fax):
	return max([drs(f) for f in fax])

top = 1000000
allFactors = getFactors(top)
pastFax = {}
sumMdrs = 0
for i in xrange(2, top):
	theFax = getFax(i, allFactors[i], pastFax)
	pastFax[i] = theFax

	sumMdrs = sumMdrs + mdrs(theFax)

print sumMdrs





