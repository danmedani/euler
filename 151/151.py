import copy

chanceOne = 0

# numSheets [#A5, #A4, #A3, #A2]
def choose(numSheets, sheetCount, chance):
  global chanceOne

  if (sheetCount == 1) and (numSheets[0] == 1):
    # print 'we done', numSheets, chance
    return
  elif sheetCount == 1:
    # print 'found just 1', numSheets, chance
    chanceOne = chanceOne + chance

  # print numSheets, sheetCount, chance
  for i in xrange(len(numSheets)):
    if numSheets[i] > 0:

      numSheetsCop = copy.deepcopy(numSheets)
      numSheetsCop[i] = numSheetsCop[i] - 1

      newSheetCount = sheetCount + i - 1
      for j in xrange(0, i):
        numSheetsCop[j] = numSheetsCop[j] + 1
      
      choose(numSheetsCop, newSheetCount, chance * (1.0 * numSheets[i] / sheetCount))


choose([1, 1, 1, 1], 4, 1.0)
print chanceOne
