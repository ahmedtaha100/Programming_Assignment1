from closest_pairs import find_m_closest
import time
import random

# Test Case 1: Simple 4 points
test1_points = [
    {'x': 0, 'y': 0},
    {'x': 1, 'y': 1},
    {'x': 3, 'y': 3},
    {'x': 5, 'y': 5}
]
result1 = find_m_closest(test1_points, 2)
print("Test 1 - Finding 2 closest pairs from 4 points:")
for pair in result1:
    print(f"Points ({pair['p1']['x']},{pair['p1']['y']}) and ({pair['p2']['x']},{pair['p2']['y']}) - Distance: {pair['dist']:.3f}")

# Test Case 2: Edge case with m = 1
test2_points = [
    {'x': 0, 'y': 0},
    {'x': 10, 'y': 0},
    {'x': 5, 'y': 0}
]
result2 = find_m_closest(test2_points, 1)
print("\nTest 2 - Finding 1 closest pair from 3 points:")
for pair in result2:
    print(f"Points ({pair['p1']['x']},{pair['p1']['y']}) and ({pair['p2']['x']},{pair['p2']['y']}) - Distance: {pair['dist']:.3f}")

# Test Case 3: Larger set
test3_points = [
    {'x': 1, 'y': 2},
    {'x': 3, 'y': 4},
    {'x': 5, 'y': 1},
    {'x': 2, 'y': 3},
    {'x': 4, 'y': 5}
]
result3 = find_m_closest(test3_points, 3)
print("\nTest 3 - Finding 3 closest pairs from 5 points:")
for pair in result3:
    print(f"Points ({pair['p1']['x']},{pair['p1']['y']}) and ({pair['p2']['x']},{pair['p2']['y']}) - Distance: {pair['dist']:.3f}")

def generate_random_points(n):
    points = []
    for i in range(n):
        points.append({'x': random.uniform(0, 100), 'y': random.uniform(0, 100)})
    return points

def measure_performance():
    test_sizes = [10, 20, 40, 80, 160]
    
    print("\n\nPerformance Testing:")
    print("n\tm\tTime (seconds)")
    print("-" * 30)
    
    for n in test_sizes:
        points = generate_random_points(n)
        m = n // 4
        
        start_time = time.time()
        find_m_closest(points, m)
        end_time = time.time()
        
        elapsed_time = end_time - start_time
        print(f"{n}\t{m}\t{elapsed_time:.6f}")

measure_performance()