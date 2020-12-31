from typing import Dict
from typing import Tuple
from collections import defaultdict
from fractions import Fraction

P2_CHANCE = {
	t: Fraction(1, 2 ** t) for t in range(1, 9)
}
P2_POINTS = {
	t: 2 ** (t - 1) for t in range(1, 9)
}

def get_moves_for_p2() -> Dict[Tuple[int, int], int]:
	p2_moves = {}
	for p1_score in range(100):
		for p2_score in range(100):
			p2_moves[(p1_score, p2_score)] = 1
	return p2_moves


p2_moves = get_moves_for_p2()

chance_of_p1_victory = Fraction(0, 1)
chance_of_p2_victory = Fraction(0, 1)

state_to_chance_of_being_here = defaultdict(int)
state_to_chance_of_being_here[(0, 0)] = Fraction(1, 1)

p1s_move = True

for i in range(1000):
	next_layer_state_to_chance_of_being_here = defaultdict(int)

	for state, chance_of_being_here in state_to_chance_of_being_here.items():
		if state[0] >= 100 and state[1] >= 100:
			raise Exception('bad state')

		if state[0] >= 100:
			chance_of_p1_victory += chance_of_being_here
			continue
		
		if state[1] >= 100:
			chance_of_p2_victory += chance_of_being_here
			continue

		if p1s_move:
			next_layer_state_to_chance_of_being_here[(state[0], state[1])] += chance_of_being_here * Fraction(1, 2)
			next_layer_state_to_chance_of_being_here[(state[0] + 1, state[1])] += chance_of_being_here * Fraction(1, 2)
		else:
			p2s_move = p2_moves[state]
			next_layer_state_to_chance_of_being_here[(state[0], state[1] + P2_POINTS[p2s_move])] += chance_of_being_here * P2_CHANCE[p2s_move]
			next_layer_state_to_chance_of_being_here[(state[0], state[1])] += chance_of_being_here * (Fraction(1, 1) - P2_CHANCE[p2s_move])

	state_to_chance_of_being_here = next_layer_state_to_chance_of_being_here
	p1s_move = not p1s_move
	print(i, 'state_size = ', len(next_layer_state_to_chance_of_being_here))


print('chance_of_p1_victory', chance_of_p1_victory)
print('chance_of_p2_victory', chance_of_p2_victory)


