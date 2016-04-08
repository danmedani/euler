import copy

options = {'s_bull': 25, 'd_bull': 50}
for i in range(1, 21):
  options['s' + str(i)] = i
  options['d' + str(i)] = 2 * i
  options['t' + str(i)] = 3 * i


wayMap = {}
def hashIt(combo):
  if len(combo) == 1:
    return combo[0]

  comboCop = copy.deepcopy(combo)
  del(comboCop[0])
  comboCop.sort()

  return combo[0] + reduce(lambda x,y: x + y, comboCop)

def waysToCheck(soFar, n):
  global wayMap

  s = 0
  if n == 0:
    hVal = hashIt(soFar)
    if hVal not in wayMap:
      wayMap[hVal] = True
      return 1
    else:
      return 0

  elif len(soFar) == 3:
    return 0
  else:
    filtOptions = [opt for opt in options if options[opt] <= n]

    for opt in filtOptions:
      soFarCop = copy.deepcopy(soFar)
      soFarCop.append(opt)
      s = s + waysToCheck(soFarCop, n - options[opt])

  return s

def waysToCheckout(n):
  s = 0
  filtOptions = [opt for opt in options if options[opt] <= n]
  
  for opt in filtOptions:
    if opt[0] == 'd':
      s = s + waysToCheck([opt], n - options[opt])

  return s

totalWays = 0
for i in xrange(1, 100):
  wayMap = {}
  ways = waysToCheckout(i)
  totalWays = totalWays + ways
  print i, ways, totalWays

print totalWays
