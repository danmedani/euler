import time

sk_map = {}
def s_k(k):
	global sk_map

	if k in sk_map:
		return sk_map[k]

	result = None
	if k <= 55:
		result = ( 100003 - (200003 * k) + (300007 * k ** 3) ) % 1000000
	else:
		result = ( s_k(k - 24) + s_k(k - 55) ) % 1000000

	sk_map[k] = result
	return result

def getCall(n):
	if n == 5:
		return 701497, 200007
	if n == 6:
		return 500439, 602383
	if n == 7:
		return 100053, 500439
	return s_k(2 * n - 1), s_k(2 * n)

# Upper bound on # of groups
max_group_number = 0

# Group # -> Group
group = {}

class Person:
	def __init__(self, personNumber, nextPerson):
		self.personNumber = personNumber
		self.nextPerson = nextPerson

class Group:
	def __init__(self):
		self.size = 0
		self.firstPerson = None
		self.lastPerson = None

	def addPerson(self, personNumber):
		if self.firstPerson == None:
			self.firstPerson = Person(personNumber, None)
			self.lastPerson = self.firstPerson
		elif self.lastPerson == None:
			self.lastPerson = Person(personNumber, None)
			self.firstPerson.nextPerson = self.lastPerson
		else:
			self.lastPerson.nextPerson = Person(personNumber, None)
			self.lastPerson = self.lastPerson.nextPerson

		self.size = self.size + 1

	def addGroup(self, newGroup):
		self.lastPerson.nextPerson = newGroup.firstPerson
		self.lastPerson = newGroup.lastPerson
		self.size = self.size + newGroup.size

	def printMe(self):
		print 'group size', self.size
		node = self.firstPerson
		while node != None:
			print node.personNumber
			node = node.nextPerson
		print ''

# Person # -> group #
personsGroup = {}


pm = 524287
n = 1
successfulCalls = 0

while True:
	caller, callee = getCall(n)

	if caller != callee:
		successfulCalls = successfulCalls + 1
		if ( caller not in personsGroup ) and ( callee not in personsGroup ):
			# 1: both personsGroup are brand new. Make a new group and stick em in it.
			group[max_group_number] = Group()
			group[max_group_number].addPerson(caller)
			group[max_group_number].addPerson(callee)

			personsGroup[caller] = max_group_number
			personsGroup[callee] = max_group_number

			max_group_number = max_group_number + 1

		elif ( caller not in personsGroup ) and ( callee in personsGroup ):
			# 2: caller is new, callee is not. Stick caller in callee's group.
			group[personsGroup[callee]].addPerson(caller)

			personsGroup[caller] = personsGroup[callee]

		elif ( caller in personsGroup ) and ( callee not in personsGroup ):
			# 3: callee is new, caller is not. Stick callee in caller's group.
			group[personsGroup[caller]].addPerson(callee)

			personsGroup[callee] = personsGroup[caller]

		else:
			if personsGroup[caller] != personsGroup[callee]:
				# 4: Both in different groups already .. merge groups.
				
				if group[personsGroup[callee]].size > group[personsGroup[caller]].size:
					group[personsGroup[callee]].addGroup(group[personsGroup[caller]])
					group_to_kill = personsGroup[caller]

					person = group[personsGroup[caller]].firstPerson
					while person != None:
						personsGroup[person.personNumber] = personsGroup[callee]
						person = person.nextPerson
					
					del(group[group_to_kill])
				else:
					group[personsGroup[caller]].addGroup(group[personsGroup[callee]])
					group_to_kill = personsGroup[callee]

					person = group[personsGroup[callee]].firstPerson
					while person != None:
						personsGroup[person.personNumber] = personsGroup[caller]
						person = person.nextPerson
					
					del(group[group_to_kill])
				


	if pm in personsGroup:
		sizePct = 1.0 * group[personsGroup[pm]].size / 1000000

		if sizePct >= .99:
			print 'got >= 99%!'
			print 'pm group size, numPeople, pct', group[personsGroup[pm]].size, len(personsGroup), sizePct
			print 'n, numGroups, numPeople, successfulCalls', n, len(group), len(personsGroup), successfulCalls
			break

	n = n + 1





