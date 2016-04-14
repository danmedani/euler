
f = open('p054_poker.txt')

hands = [s.split(' ') for s in [line[0:len(line)-1] for line in f.readlines()]]

def getHand1(hand):
  return hand[0:5]
def getHand2(hand):
  return hand[5:10]

def getCardVal(card):
  val = card[0]
  if val == 'A':
    return 14
  if val == 'K':
    return 13
  if val == 'Q':
    return 12
  if val == 'J':
    return 11
  if val == 'T':
    return 10
  return int(val)

def getMaxCardVal(hand):
  cards = [getCardVal(card) for card in hand]
  return max(cards)

def getMaxCardValMinusAce(hand):
  cards = [getCardVal(card) for card in hand]
  while 14 in cards:
    cards.remove(14)
  return max(cards)

def getCardValCounts(hand):
  cardValCount = {}
  for card in hand:
    v = getCardVal(card)
    if v not in cardValCount:
      cardValCount[v] = 1
    else:
      cardValCount[v] = cardValCount[v] + 1
  return cardValCount

def isFlush(hand):
  suits = [card[1] for card in hand]
  s = suits[0]
  for suit in suits:
    if suit != s:
      return False

  return True

def isStraight(hand):
  if isTwoPairs(hand) or isOnePair(hand) or isThreeOfKind(hand):
    return False

  vals = [getCardVal(card) for card in hand]
  vals.sort()
  if 14 in vals:
    if 2 in vals:
      return getMaxCardValMinusAce(hand) == 5

  return vals[4] - vals[0] == 4

def isStraightFlush(hand):
  return isStraight(hand) and isFlush(hand)
def isFourOfAKind(hand):
  cardValCounts = getCardValCounts(hand)
  for key in cardValCounts:
    if cardValCounts[key] == 4:
      return True
  return False
def isFullHouse(hand):
  hasThree = False
  hasTwo = False
  cardValCounts = getCardValCounts(hand)
  for key in cardValCounts:
    if cardValCounts[key] == 3:
      hasThree = True
    if cardValCounts[key] == 2:
      hasTwo = True

  return hasTwo and hasThree

def isThreeOfKind(hand):
  cardValCounts = getCardValCounts(hand)

  for key in cardValCounts:
    if (cardValCounts[key] == 3) and len(cardValCounts) > 2:
      return True

  return False

def isTwoPairs(hand):
  cardValCounts = getCardValCounts(hand)

  for key in cardValCounts:
    if (cardValCounts[key] == 2) and len(cardValCounts) == 3:
      return True

  return False  

def isOnePair(hand):
  cardValCounts = getCardValCounts(hand)

  for key in cardValCounts:
    if (cardValCounts[key] == 2) and len(cardValCounts) == 4:
      return True

  return False  


def getVal(hand):
  if isStraightFlush(hand):
    vals = [getCardVal(card) for card in hand]

    if 14 in vals:
      if 2 in vals:
        return (10 ** 14) + getMaxCardValMinusAce(hand)

    return (10 ** 14) + getMaxCardVal(hand)
  if isFourOfAKind(hand):
    cardValCounts = getCardValCounts(hand)

    fourVal = 0
    oneVal = 0

    for key in cardValCounts:
      if cardValCounts[key] == 4:
        fourVal = key
      else:
        oneVal = key
    return (10 ** 13) + (100 * fourVal) + oneVal
  if isFullHouse(hand):
    cardValCounts = getCardValCounts(hand)

    threeVal = 0
    twoVal = 0

    for key in cardValCounts:
      if cardValCounts[key] == 3:
        threeVal = key
      else:
        oneVal = key
    return (10 ** 12) + (100 * threeVal) + oneVal
  if isFlush(hand):
    cardValCounts = getCardValCounts(hand)
    max1 = max2 = max3 = max4 = max5 = 0
    for i in xrange(14, 1, -1):
      if i in cardValCounts:
        if max1 == 0:
          max1 = i
        elif max2 == 0:
          max2 = i
        elif max3 == 0:
          max3 = i
        elif max4 == 0:
          max4 = i
        elif max5 == 0:
          max5 = i

    return (10 ** 11) + (60000 * max1) + (3375 * max2) + (225 * max3) + (15 * max4) + max5
  if isStraight(hand):
    vals = [getCardVal(card) for card in hand]

    if 14 in vals:
      if 2 in vals:
        return (10 ** 10) + getMaxCardValMinusAce(hand)

    return (10 ** 10) + getMaxCardVal(hand)
  if isThreeOfKind(hand):
    cardValCounts = getCardValCounts(hand)

    tripVal = 0
    oneVal = 0
    theOtherVal = 0

    for key in cardValCounts:
      if cardValCounts[key] == 3:
        tripVal = key
      elif oneVal == 0:
        oneVal = key
      else:
        theOtherVal = key
    return (10 ** 9) + (100 * tripVal) + max(oneVal, theOtherVal)
  if isTwoPairs(hand):
    cardValCounts = getCardValCounts(hand)

    dub1Val = 0
    dub2Val = 0
    theOtherVal = 0

    for key in cardValCounts:
      if (dub1Val == 0) and cardValCounts[key] == 2:
        dub1Val = key
      elif cardValCounts[key] == 2:
        dub2Val = key
      else:
        theOtherVal = key

    return (10 ** 8) + (225 * max(dub1Val, dub2Val)) + (15 * min(dub1Val, dub2Val)) + theOtherVal
  if isOnePair(hand):
    cardValCounts = getCardValCounts(hand)

    dubVal = 0
    theOtherVal1 = 0
    theOtherVal2 = 0
    theOtherVal3 = 0

    for key in cardValCounts:
      if cardValCounts[key] == 2:
        dubVal = key
      elif theOtherVal1 == 0:
        theOtherVal1 = key
      elif theOtherVal2 == 0:
        theOtherVal2 = key
      else:
        theOtherVal3 = key

    big = max(theOtherVal1, theOtherVal2, theOtherVal3)
    small = min(theOtherVal1, theOtherVal2, theOtherVal3)
    medium = theOtherVal3 + theOtherVal2 + theOtherVal1 - big - small

    return (10 ** 7) + (3375 * dubVal) + (225 * big) + (15 * medium) + small
  
  # nothing
  cardValCounts = getCardValCounts(hand)
  max1 = max2 = max3 = max4 = max5 = 0
  for i in xrange(14, 1, -1):
    if i in cardValCounts:
      if max1 == 0:
        max1 = i
      elif max2 == 0:
        max2 = i
      elif max3 == 0:
        max3 = i
      elif max4 == 0:
        max4 = i
      elif max5 == 0:
        max5 = i

  return (60000 * max1) + (3375 * max2) + (225 * max3) + (15 * max4) + max5

def isHand1Better(hand1, hand2):
  h1 = getVal(hand1)
  h2 = getVal(hand2)
  return h1 > h2


s = 0
for hand in hands:
  if isHand1Better(getHand1(hand), getHand2(hand)):
    s = s + 1
print s
