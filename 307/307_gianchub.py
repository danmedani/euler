from collections import defaultdict
# adapted from gianchub, https://projecteuler.net/thread=307#34027

# chips, defects = 10**6, 2*10**4
chips, defects = 7, 3

defects_layer = defaultdict(int)
defects_layer[ (chips, 0) ] = 1

for i in range(defects):
    print('start', defects_layer)
    next_layer = defaultdict(int)

    for defects, chance in defects_layer.items():
        if defects[0] > 0:
            # move chip from 0 to 1
            next_layer[ (defects[0] - 1, defects[1] + 1) ] += ( defects[0] * chance ) / chips

        if defects[1] > 0:
            # move chip from 1 to ?
            next_layer[ (defects[0], defects[1] - 1) ] += ( defects[1] * chance ) / chips

    defects_layer = next_layer
    print('end', next_layer)
    print()

r = 1.0 - sum(defects_layer.values())

print('Solution: {0:.10f}'.format(r))



