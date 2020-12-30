from typing import List
from collections import defaultdict
from copy import deepcopy

not_color = {
	1: [2, 3],
	2: [1, 3],
	3: [1, 2]
}

not_colors = {
	(1, 3): 2,
	(3, 1): 2,
	(2, 1): 3,
	(1, 2): 3,
	(2, 3): 1,
	(3, 2): 1
}


def get_not_colors(color: int) -> List[int]:
	return deepcopy(not_color[color])

def get_not_color_two(color_a: int, color_b: int) -> int:
	return not_colors[(color_a, color_b)]

def append_color(colors: int, new_color: int) -> int:
	return (colors * 10) + new_color

def append_two_colors(existing_list: List[int], first_color: int, second_color: int) -> List[int]:
	dupe_new_layers = deepcopy(existing_list)
	for i in range(len(existing_list)):
		existing_list[i] = append_color(existing_list[i], first_color)
	for i in range(len(dupe_new_layers)):
		dupe_new_layers[i] = append_color(dupe_new_layers[i], second_color)
	return existing_list + dupe_new_layers


def extract_colors(layer: int) -> List[int]:
	colors = []
	while layer > 0:
		colors.append(layer % 10)
		layer = int(layer / 10)
	colors.reverse()
	return colors


def generate_new_layers(layer: int, down_facing: bool) -> List[int]:
	new_layers: List[int] = []
	colors = extract_colors(layer)
	if not down_facing:
		for color in colors:
			first_color, second_color = get_not_colors(color)
			if len(new_layers) == 0:
				new_layers.append(0)
			new_layers = append_two_colors(new_layers, first_color, second_color)
	else:
		new_layers = get_not_colors(colors[0])
		for i in range(0, len(colors) - 1):
			same_color = colors[i] == colors[i + 1]
			if not same_color:
				new_color = get_not_color_two(colors[i], colors[i + 1])
				for i in range(len(new_layers)):
					new_layers[i] = append_color(new_layers[i], new_color)
			else:
				first_color, second_color = get_not_colors(colors[i])
				new_layers = append_two_colors(new_layers, first_color, second_color)
		first_color, second_color = get_not_colors(colors[len(colors) - 1])
		new_layers = append_two_colors(new_layers, first_color, second_color)

	return new_layers


layer_ways = defaultdict(int)
layer_ways[1] = 1
layer_ways[2] = 1
layer_ways[3] = 1


down_facing = False

for i in range(14):
	next_layer_ways = defaultdict(int)

	for layer_hash, ways in layer_ways.items():
		for new_layer in generate_new_layers(layer_hash, down_facing):
			next_layer_ways[new_layer] += ways

	down_facing = not down_facing
	layer_ways = next_layer_ways


print(len(layer_ways))
print('distinct options last layer', len(layer_ways))
print('ways = {}'.format(sum(layer_ways.values())))
# print(layer_ways)




