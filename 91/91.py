#!/usr/bin/python
import math

n = 50

def same(Ax, Ay, Bx, By):
	return (Ax == Bx and Ay == By)

def getLine(Ax, Ay, Bx, By):
	b = 1.0 * ((Bx*Ay) - (Ax*By)) / (Bx - Ax)
	if (Ax == 0):
		s = 1.0 * (By - b) / Bx
	else:
		s = 1.0 * (Ay - b) / Ax
	return s, b

def isPerp(s1, s2):
	if (s1 * s2 == 0):
		return False
	if (s2 > 0):
		return (abs(s1 - (-1.0 * (1.0 / s2))) < 0.0000000001)
	else:
		return (abs(s2 - (-1.0 * (1.0 / s1))) < 0.0000000001)

def hasRight(Ax, Ay, Bx, By):
	global s, n

	s, b = getLine(Ax, Ay, Bx, By)
	if (Ax > 0):
		sA, bA = getLine(0, 0, Ax, Ay)
		if (isPerp(sA, s)):
			return True
	return False

d = 0
for Ax in xrange(0, n+1):
	for Ay in xrange(0, n+1):
		for Bx in xrange(0, n+1):
			for By in xrange(0, n+1):
				if (not same(Ax, Ay, Bx, By)):
					if (not (Ax == Bx or Ay == By)):
						if (not ((Ax == 0 and Ay == 0) or (Bx == 0 and By == 0))):
							if (not ((Ax + By == 0) or (Ay + Bx == 0))):
								if (hasRight(Ax, Ay, Bx, By)):
									d = d + 1

print (3 * (n ** 2)) + d
