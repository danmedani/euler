#!/usr/bin/python

f = open('p083_matrix.txt', 'r')

mat = []
for line in f:
	l = line[0:len(line)-1]
	mat.append(map(int, l.split(',')))

def printMat(mat):
	for i in xrange(len(mat)):
		print mat[i]

tentative = []
for i in xrange(len(mat)):
	li = []
	for j in xrange(len(mat[i])):
		li.append(10**10)
	tentative.append(li)

q = [(0, 0)]
visited = []

def addToQ(i, j):
	global q, tentative

	if ((i, j) not in q):
		x = 0
		while x < len(q):
			qElem = q[x]
			if (tentative[qElem[0]][qElem[1]] > tentative[i][j]):
				break
			
			x = x + 1

		q.insert(x, (i, j))

def visitNode(i, j):
	global q, tentative, visited

	if (i < (len(mat) - 1)):
		if ((i+1, j) not in visited):
			newMin = min(tentative[i+1][j], tentative[i][j] + mat[i+1][j])
			tentative[i+1][j] = newMin
			addToQ(i+1, j)

	if (j < (len(mat[i]) - 1)):
		if ((i, j+1) not in visited):
			newMin = min(tentative[i][j+1], tentative[i][j] + mat[i][j+1])
			tentative[i][j+1] = newMin
			addToQ(i, j+1)

	if (i > 0):
		if ((i-1, j) not in visited):
			newMin = min(tentative[i-1][j], tentative[i][j] + mat[i-1][j])
			tentative[i-1][j] = newMin
			addToQ(i-1, j)

	if (j > 0):
		if ((i, j-1) not in visited):
			newMin = min(tentative[i][j-1], tentative[i][j] + mat[i][j-1])
			tentative[i][j-1] = newMin
			addToQ(i, j-1)

tentative[0][0] = mat[0][0]
while len(q) > 0:
	n = q.pop(0)
	visitNode(n[0], n[1])
	visited.append(n)
	
print tentative[79][79]