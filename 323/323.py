import math

def choose(a, b):
  return math.factorial(a) / (math.factorial(b) * math.factorial(a - b))

def f(a, b, n):
  num = (2 ** a) * choose(n - a, b - a)
  denom = 2 ** n

  return 1.0 * num / denom

dig = 32

eMap = {
  dig: 0
}
def e(a, n):
  if a in eMap:
    return eMap[a]

  if a == n:
    return 0

  ev = 0
  
  stayEv = 0.0
  chanceNoMove = f(a, a, n)
  
  for numNoMoves in xrange(100):
    for i in xrange(a+1, n+1):
      ev = ev + ( ( e(i, n) + numNoMoves + 1 )      *           (chanceNoMove ** numNoMoves) * f(a, i, n) )


  retVal = stayEv + ev
  eMap[a] = retVal

  return retVal

for i in xrange(dig - 1, -1, -1):
  print i, '->', dig, ' : ', e(i, dig)
