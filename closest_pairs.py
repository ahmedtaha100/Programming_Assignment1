import math

def find_m_closest(points_set, num_pairs):
    total_points = len(points_set)
    pair_distances = []
    
    first_idx = 0
    while first_idx < total_points - 1:
        second_idx = first_idx + 1
        while second_idx < total_points:
            x_diff = points_set[first_idx]['x'] - points_set[second_idx]['x']
            y_diff = points_set[first_idx]['y'] - points_set[second_idx]['y']
            euclidean_dist = math.sqrt(x_diff * x_diff + y_diff * y_diff)
            pair_info = {
                'dist': euclidean_dist,
                'p1': points_set[first_idx],
                'p2': points_set[second_idx]
            }
            pair_distances.append(pair_info)
            second_idx = second_idx + 1
        first_idx = first_idx + 1
    
    pair_distances.sort(key=lambda x: x['dist'])
    
    closest_pairs = []
    counter = 0
    while counter < num_pairs:
        closest_pairs.append(pair_distances[counter])
        counter = counter + 1
    
    return closest_pairs