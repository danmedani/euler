import operator
import copy

possMap = {}

def getPosPossUtil(lenL, nums, soFar, index, endList):
  if nums == 0:
    endList.append(copy.deepcopy(soFar))
  else:
    if index + nums > len(soFar):
      return
    else:
      for i in xrange(index, len(soFar)):
        soFar[i] = True
        getPosPossUtil(lenL, nums - 1, soFar, i + 1, endList)
        soFar[i] = False

def getPosPoss(lenL, nums):
  if nums in possMap:
    return possMap[nums]

  endList = []
  getPosPossUtil(lenL, nums, [False] * lenL, 0, endList)
  possMap[nums] = endList
  return endList

def initPossibility(cnt):
  possibility = []
  for i in xrange(cnt):
    possibility.append([True] * 10)
  return possibility

def isLegitPosition(positionSet, guess, possibility):
  for i in xrange(len(positionSet)):
    if positionSet[i]:
      if not possibility[i][guess[i]]:
        return False
    else:
      if possibility[i][guess[i]]:
        if sum([1 for x in xrange(len(possibility[i])) if possibility[i][x]]) == 1:
          return False
  
  return True

def modPossibility(positionSet, guess, ogPossibility):
  possibility = copy.deepcopy(ogPossibility)
  for i in xrange(len(positionSet)):
    if positionSet[i]: 
      for x in xrange(len(possibility[i])):
        if x != guess[i]:
          possibility[i][x] = False
    else: 
      possibility[i][guess[i]] = False
  return possibility


def reducePoss(possibility):
  ans = []
  for i in xrange(len(possibility)):
    for j in xrange(len(possibility[i])):
      if possibility[i][j]:
        ans.append(j)
  if len(ans) == len(possibility):
    return ans
  else:
    return []

maxIndex = -1
def find(guesses, numCorrect, index, possibility):
  if index == len(guesses):
    red = reducePoss(possibility)
    if len(red) > 0:
      print 'got it', red
  else:
    guess = guesses[index]
    possiblePositions = getPosPoss(len(possibility), numCorrect[index])
    for positionSet in possiblePositions:
      if isLegitPosition(positionSet, guess, possibility):
        modPoss = modPossibility(positionSet, guess, possibility)
        find(guesses, numCorrect, index + 1, modPoss)

g = [
  ([5,6,1,6,1,8,5,6,5,0,5,1,8,2,9,3],2),
  ([3,8,4,7,4,3,9,6,4,7,2,9,3,0,4,7],1),
  ([5,8,5,5,4,6,2,9,4,0,8,1,0,5,8,7],3),
  ([9,7,4,2,8,5,5,5,0,7,0,6,8,3,5,3],3),
  ([4,2,9,6,8,4,9,6,4,3,6,0,7,5,4,3],3),
  ([3,1,7,4,2,4,8,4,3,9,4,6,5,8,5,8],1),
  ([4,5,1,3,5,5,9,0,9,4,1,4,6,1,1,7],2),
  ([7,8,9,0,9,7,1,5,4,8,9,0,8,0,6,7],3),
  ([8,1,5,7,3,5,6,3,4,4,1,1,8,4,8,3],1),
  ([2,6,1,5,2,5,0,7,4,4,3,8,6,8,9,9],2),
  ([8,6,9,0,0,9,5,8,5,1,5,2,6,2,5,4],3),
  ([6,3,7,5,7,1,1,9,1,5,0,7,7,0,5,0],1),
  ([6,9,1,3,8,5,9,1,7,3,1,2,1,3,6,0],1),
  ([6,4,4,2,8,8,9,0,5,5,0,4,2,7,6,8],2),
  ([2,3,2,1,3,8,6,1,0,4,3,0,3,8,4,5],0),
  ([2,3,2,6,5,0,9,4,7,1,2,7,1,4,4,8],2),
  ([5,2,5,1,5,8,3,3,7,9,6,4,4,3,2,2],2),
  ([1,7,4,8,2,7,0,4,7,6,7,5,8,2,7,6],3),
  ([4,8,9,5,7,2,2,6,5,2,1,9,0,3,0,6],1),
  ([3,0,4,1,6,3,1,1,1,7,2,2,4,6,3,5],3),
  ([1,8,4,1,2,3,6,4,5,4,3,2,4,5,8,9],3),
  ([2,6,5,9,8,6,2,6,3,7,3,1,6,8,6,7],2)
]

print len(g)
g = sorted(g, key=operator.itemgetter(1))

possibility = initPossibility(len(g[0][0]))
guesses = [f[0] for f in g]
numCorrect = [f[1] for f in g]

find(guesses, numCorrect, 0, possibility)



