
def u(k, r):
  return (900 - (3 * k)) * (r ** (k - 1))

def s(n, r):
  ssum = 0 
  for i in xrange(1, n+1):
    ssum = ssum + u(i, r)
  return ssum

n = 5000
r = 1.00232210863287
ss = s(n, r)
print n, r, ss, ss / -1000000000


