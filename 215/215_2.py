import copy

width = 32
height = 10

def hashLayer(layer):
  ret = ''
  for block in layer:
    ret = ret + str(block) + '-'
  return ret

layers = []
layerMap = {}

def addLayer(layer):
  global layerMap

  hVal = hashLayer(layer)
  if hVal not in layerMap:
    layerMap[hVal] = True
    layers.append(copy.deepcopy(layer))

def buildLayer(spaceLeft, layerSoFar):
  global layers

  if spaceLeft < 2:
    return
  
  if spaceLeft == 2:
    layerSoFar.append(2)
    addLayer(layerSoFar)
    layerSoFar.pop()
  elif spaceLeft == 3:
    layerSoFar.append(3)
    addLayer(layerSoFar)
    layerSoFar.pop()
  else:
    # try 2
    layerSoFar.append(2)
    buildLayer(spaceLeft - 2, layerSoFar)
    layerSoFar.pop()

    layerSoFar.append(3)
    buildLayer(spaceLeft - 3, layerSoFar)
    layerSoFar.pop()

buildLayer(width, [])

def getCrack(layer):
  crack = []
  x = 0
  for i in xrange(len(layer) - 1):
    crack.append(x + layer[i])
    x = x + layer[i]
  return crack

def getCrackMap(layer):
  crackMap = {}
  x = 0
  for i in xrange(len(layer) - 1):
    crackMap[x + layer[i]] = True
    x = x + layer[i]
  return crackMap

cracks = [ getCrack(layer) for layer in layers ]
crackMap = [ getCrackMap(layer) for layer in layers ]

def fits(newCracks, oldCrackMap):
  for crack in newCracks:
    if crack in oldCrackMap:
      return False
  return True

nodeGraph = {}
for i in xrange(len(crackMap)):  
  nodeGraph[i] = []
  for j in xrange(len(crackMap)):
    if fits(crackMap[i], crackMap[j]):
      nodeGraph[i].append(j)


def hashIt(layer, height):
  return (layer * 10000) + height

dp = {}

def build(lastLayer, currentHeight):
  hVal = hashIt(lastLayer, currentHeight)
  
  if hVal in dp:
    return dp[hVal]

  if currentHeight == height:
    dp[hVal] = 1
    return 1
  else:
    ans = 0
    if lastLayer < 0:
      # first layer.
      for key in nodeGraph:
        ans = ans + build(key, currentHeight + 1)
    else:
      for neighbor in nodeGraph[lastLayer]:
        ans = ans + build(neighbor, currentHeight + 1)
    
    dp[hVal] = ans
    return ans

print build(-1, 0)




