mappins = {}

for a in xrange(1, 580):
  delta = (a * 4) - 1
  val = 0
  while delta > (-2 * (a - 1)):
    val = val + delta

    delta = delta - 2

    # don't break... it will come back down
    if val < 1000000:
      if val in mappins:
        mappins[val] = mappins[val] + 1
      else:
        mappins[val] = 1

for a in xrange(580, 250001):
  delta = (a * 4) - 1
  val = 0
  while delta > (-2 * (a - 1)):
    val = val + delta
    delta = delta - 2

    # break... it aint comin back down
    if val >= 1000000:
      break

    if val in mappins:
      mappins[val] = mappins[val] + 1
    else:
      mappins[val] = 1

s10 = 0
for key in mappins:
  if mappins[key] == 10:
    s10 = s10 + 1

print s10



