mappins = {}

for a in xrange(1, 4084):
  delta = (a * 4) - 1
  val = 0

  while delta > (-2 * (a - 1)):
    val = val + delta

    delta = delta - 2

    # don't break... it will come back down
    if val < 50000000:
      if val in mappins:
        mappins[val] = mappins[val] + 1
      else:
        mappins[val] = 1
print 'ok'
for a in xrange(4084, 12500001):
  if a % 10000 == 0:
    print a

  delta = (a * 4) - 1
  val = 0
  while delta > (-2 * (a - 1)):
    val = val + delta
    delta = delta - 2

    # break... it aint comin back down
    if val >= 50000000:
      break

    if val in mappins:
      mappins[val] = mappins[val] + 1
    else:
      mappins[val] = 1

print mappins[20], ' o yess'

s1 = 0
for key in mappins:
  if mappins[key] == 1:
    s1 = s1 + 1

print s1
# 


