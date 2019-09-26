import math
from random import randrange

def make_groups(people=[], max_size=1):
	groupCount = int(math.ceil(float(len(people)) / max_size))

	groups = [[] for _ in range(groupCount)]

	chosen = []

	def chooseRandom():
		randNum = randrange(len(people))
		while randNum in chosen:
			randNum = randrange(len(people))
		return randNum

	index = 0

	while len(chosen) < len(people):
		personIndex = chooseRandom()

		groups[index % groupCount].append(people[personIndex])

		chosen.append(personIndex)
		index += 1

	return groups
