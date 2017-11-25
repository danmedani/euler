def getRow(x):
	row = [1]

	top = x
	bottom = 1
	
	for i in xrange(1, (x / 2) + 1):
		row.append(top / bottom)
		bottom = bottom * (i+1)
		top = top * (x - i)

	for val in reversed(row):
		row.append(val)

	if x % 2 == 0:
		del(row[len(row) / 2])
		
	return row

def roll(amt, f, tosses, i):
	for i in xrange(len(tosses)):
		if tosses[i] == 0:
			amt = amt - (f * amt)
		else:
			amt = amt + (2 * f * amt)

	return amt

def getRoll(numWins, numTosses):
	return [0] * (numTosses - numWins) + [1] * numWins


def getNumOverFloor(numTosses, f, floor):
	pascalRow = getRow(numTosses)
	cnt = 0

	numWins = 0
	while numWins <= numTosses:
		amt = roll(1, f, getRoll(numWins, numTosses), 0)
		if amt > floor:
			cnt = cnt + pascalRow[numWins]

		numWins = numWins + 1

	return cnt
		

num = 1.0
maxxyF, maxxyAmt = -1, 0
f = 0.142

while f > .1:
	f = f - 0.01

	numOverFloor = getNumOverFloor(1000, f, 1000000000)
	if numOverFloor > maxxyAmt:
		maxxyAmt = numOverFloor
		maxxyF = f
		print maxxyF


print maxxyAmt
print 1.0 * maxxyAmt / (2 ** 1000)







