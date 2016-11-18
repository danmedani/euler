
perfectSquares = []
perfectSquaresMap = {}
for i in xrange(1, 10000):
  squareVal = i ** 2

  perfectSquares.append(squareVal)
  perfectSquaresMap[squareVal] = True


abcList = []
for i in xrange(len(perfectSquares)):
  for j in xrange(len(perfectSquares)):
    sumSquare = perfectSquares[i] + perfectSquares[j]
    if sumSquare in perfectSquaresMap:
      abcList.append((perfectSquares[i], perfectSquares[j], sumSquare))


lowestSoFar = 16393291639329

for sqaure in perfectSquares:
  for i in xrange(len(abcList)):

    top = sqaure - abcList[i][0]

    if (top > 0):
      if (top % 2 == 0):
        z = top / 2

        # Check the other two
        p2 = (2 * z) + abcList[i][0] + abcList[i][1]

        if (p2 in perfectSquaresMap):

          p3 = (2 * z) + (2 * abcList[i][0]) + abcList[i][1]

          # print abcList[i], z

          if (p3 in perfectSquaresMap):
            sumVal = (3 * z) + (2 * abcList[i][0]) + abcList[i][1]
            print 'got it', abcList[i], z, sumVal

            if sumVal < lowestSoFar:
              print 'NEW LOW', abcList[i], z, sumVal
              lowestSoFar = sumVal

      