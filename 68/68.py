#!/usr/bin/python
import copy

def checkConfig(c):
	if (len(c) > 2):
		val = c[0] + c[1] + c[2]
		if ((len(c) > 4) and c[2] + c[3] + c[4] != val):
			return False
		if ((len(c) > 6) and c[4] + c[5] + c[6] != val):
			return False
		if ((len(c) > 8) and c[6] + c[7] + c[8] != val):
			return False
		if ((len(c) > 9) and c[8] + c[9] + c[1] != val):
			return False
		if ((len(c) > 9) and ((c[3] < c[0]) or (c[5] < c[0]) or (c[7] < c[0]) or (c[9] < c[0]))):
			return False
	return True

def getValue(c):
	s = ''
	s = s + str(c[0])
	s = s + str(c[1])
	s = s + str(c[2])
	
	s = s + str(c[3])
	s = s + str(c[2])
	s = s + str(c[4])
	
	s = s + str(c[5])
	s = s + str(c[4])
	s = s + str(c[6])

	s = s + str(c[7])
	s = s + str(c[6])
	s = s + str(c[8])

	s = s + str(c[9])
	s = s + str(c[8])
	s = s + str(c[1])

	if (len(s) == 16):
		return int(s)
	else:
		return -1

# [2 3 6 7 8 9] [1 4 5]
# [1 4 5 2]
maxVal = 0
def runThis(bag, soFar):
	global maxVal
	
	if (not checkConfig(soFar)):
		return

	if (len(bag) == 0):
		val = getValue(soFar)
		if (val > maxVal):
			maxVal = val
			print maxVal, soFar


	for i in xrange(len(bag)):
		soFarCopy = copy.deepcopy(soFar)
		bagCopy = copy.deepcopy(bag)
		soFarCopy.append(bagCopy.pop(i))
		runThis(bagCopy, soFarCopy)

bag = [1, 4, 3, 2, 7, 6, 5, 8, 9, 10]
runThis(bag, [])
