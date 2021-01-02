from typing import Dict
from typing import Tuple
from collections import defaultdict
# from fractions import Fraction

P2_CHANCE = {
	t: 1.0 / (2 ** t) for t in range(1, 9)
}
P2_POINTS = {
	t: 2 ** (t - 1) for t in range(1, 9)
}

def get_chance_of_p2_victory(
	starting_state: Tuple[int, int],
	p2_moves: Dict[Tuple[int, int], int],
	p1s_move: bool
) -> float:
	chance_of_p1_victory = 0
	chance_of_p2_victory = 0
	total_chance = chance_of_p1_victory + chance_of_p2_victory
	state_to_chance_of_being_here = defaultdict(int)
	state_to_chance_of_being_here[starting_state] = 1.0

	while total_chance < 0.9999999999:
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
				next_layer_state_to_chance_of_being_here[(state[0], state[1])] += chance_of_being_here * 1.0 / 2
				next_layer_state_to_chance_of_being_here[(state[0] + 1, state[1])] += chance_of_being_here * 1.0 / 2
			else:
				p2s_move = p2_moves[state]
				next_layer_state_to_chance_of_being_here[(state[0], state[1] + P2_POINTS[p2s_move])] += chance_of_being_here * P2_CHANCE[p2s_move]
				next_layer_state_to_chance_of_being_here[(state[0], state[1])] += chance_of_being_here * (1.0 - P2_CHANCE[p2s_move])

		state_to_chance_of_being_here = next_layer_state_to_chance_of_being_here
		p1s_move = not p1s_move
		total_chance = chance_of_p1_victory + chance_of_p2_victory
	return chance_of_p2_victory


p2_moves = {}

for p2_score in range(99, -1, -1):
	p1_score = 99
	while p1_score >= 0:
		# find the best!
		best_move = -1	
		best_move_chance = -1
		for p2_move in range(1, 9):
			p2_moves[(p1_score, p2_score)] = p2_move
			chance_of_p2_victory = get_chance_of_p2_victory((p1_score, p2_score), p2_moves, False)
			if chance_of_p2_victory > best_move_chance:
				best_move_chance = chance_of_p2_victory
				best_move = p2_move

		print('best move for ({}, {}) = {} ({})'.format(
			p1_score, 
			p2_score,
			best_move,
			best_move_chance
		))
		p2_moves[p1_score, p2_score] = best_move

		if best_move == 1: # the rest are prolly 1
			while p1_score >= 0:
				p2_moves[p1_score, p2_score] = 1
				p1_score -= 1

		p1_score -= 1


print(p2_moves)


