#!/usr/bin/python

maxNumPicks = 20
numColors = 7
numBallsEachColor = 10

pctChance = {
	1: 0,
	2: 0,
	3: 0,
	4: 0,
	5: 0,
	6: 0,
	7: 0,
	8: 0,
	9: 0,
	10: 0
}

def combinate(numSeen, numUnSeen, distinctCount, pickNum, pct):
	if (pickNum > maxNumPicks):
		pctChance[distinctCount] = pctChance[distinctCount] + pct
	else:
		if (numUnSeen > 0):
			combinate(numSeen + numBallsEachColor - 1, numUnSeen - numBallsEachColor, distinctCount + 1, pickNum + 1, pct * (1.0 * numUnSeen / (numUnSeen + numSeen)))
		if (numSeen > 0):
			combinate(numSeen - 1, numUnSeen, distinctCount, pickNum + 1, pct * (1.0 * numSeen / (numUnSeen + numSeen)))

combinate(0, numBallsEachColor * numColors, 0, 1, 1.0)
print pctChance

expect = 0
for ballCount in pctChance.keys():
	expect = expect + (pctChance[ballCount] * ballCount)

print expect