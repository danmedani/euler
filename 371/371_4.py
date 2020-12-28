from collections import defaultdict

# (losers, opportunities, mid-points, winners)
chances_of_being_here_layer = defaultdict(int)
chances_of_being_here_layer[ (1, 998, 1, 0) ] = 1.0

expected_val = 0.0

for plate_count in range(1, 500):
    
    next_layer = defaultdict(int)

    for type_counts, chances_of_being_here in chances_of_being_here_layer.items():
        losers, opportunities, mid_points, winners = type_counts

        expected_val += chances_of_being_here * plate_count * (1.0 * winners / 1000)
        
        if losers > 0:
            next_layer[ (losers, opportunities, mid_points, winners) ] += (chances_of_being_here * (1.0 * losers / 1000))

        if opportunities > 0:
            next_layer[ (losers + 1, opportunities - 2, mid_points, winners + 1) ] += (chances_of_being_here * (1.0 * opportunities / 1000))

        if mid_points > 0:
            next_layer[ (losers, opportunities, mid_points - 1, winners + 1) ] += (chances_of_being_here * (1.0 * mid_points / 1000))

    chances_of_being_here_layer = next_layer
    print('Expected_val: {0:.10f}'.format(expected_val))


