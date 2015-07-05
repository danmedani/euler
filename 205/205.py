#!/usr/bin/python

fourSideMap = {}
sixSideMap = {}

def roll(diceCount, diceSides, total, totalMap):
	if (diceCount == 0):
		if (total in totalMap):
			totalMap[total] = totalMap[total] + 1
		else:
			totalMap[total] = 1
	else:
		for i in xrange(1, diceSides + 1):
			totalMap = roll(diceCount - 1, diceSides, total + i, totalMap)
	return totalMap


def getTotal(chances):
	total = 0
	for key in chances.keys():
		total = total + chances[key]	
	return total

def chanceOfBeatingColin(num, colinChances, colinTotal):
	i = 6
	chance = 0
	while i < num:
		if (i not in colinChances):
			break
		chance = chance + (1.0 * colinChances[i] / colinTotal)
		i = i + 1
	return chance

def timesBeatColin(num, colinChances):
	i = 6
	chance = 0
	while i < num:
		if (i not in colinChances):
			break
		chance = chance + colinChances[i]
		i = i + 1
	return chance

peteChances = roll(9, 4, 0, fourSideMap)
colinChances = roll(6, 6, 0, sixSideMap)
peteTotal = getTotal(peteChances)
colinTotal = getTotal(colinChances)

print peteChances, getTotal(peteChances)
print colinChances, getTotal(colinChances)

timesWon = 0
totalTimes = 0
for peteKey in peteChances.keys():
	timesWon = timesWon + (peteChances[peteKey] * timesBeatColin(peteKey, colinChances))

print timesWon
print peteTotal * colinTotal
print 1.0 * timesWon / (peteTotal * colinTotal)
