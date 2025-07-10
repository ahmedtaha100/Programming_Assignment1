```markdown
# Closest Pairs Algorithm

## Overview
This program finds the m closest pairs of points from a set of n points in a 2D plane using Euclidean distance.

## Installation Requirements
- Python 3.x must be installed on your system
- No additional packages needed - only Python standard library (math, time, random)

## How to Run

1. Clone or download all files to the same directory
2. Open terminal/command prompt in that directory
3. Run the test program:
   ```bash
   python3 test_closest_pairs.py
   ```
   Or on Windows:
   ```bash
   python test_closest_pairs.py
   ```

## Input Data Format

The algorithm requires two inputs:

1. **points_set**: A list of point dictionaries
   - Each point must have 'x' and 'y' keys with numeric values
   - Example:
   ```python
   points = [
       {'x': 0, 'y': 0},    # Point 1
       {'x': 1, 'y': 1},    # Point 2
       {'x': 3, 'y': 3}     # Point 3
   ]
   ```

2. **num_pairs**: Integer specifying how many closest pairs to return
   - Must be ≤ n(n-1)/2 where n is number of points
   - Example: `m = 2` to get 2 closest pairs

## Output Data Format

Returns a list of dictionaries, each containing:
```python
{
    'dist': 1.414,                    # Euclidean distance
    'p1': {'x': 0, 'y': 0},          # First point
    'p2': {'x': 1, 'y': 1}           # Second point
}
```

## Using in Your Own Code

```python
from closest_pairs import find_m_closest

# Prepare your points
my_points = [
    {'x': 0, 'y': 0},
    {'x': 1, 'y': 1},
    {'x': 3, 'y': 3}
]

# Call the function
result = find_m_closest(my_points, 2)  # Get 2 closest pairs

# Process results
for pair in result:
    print(f"Distance: {pair['dist']}")
```

## Expected Test Output

Running `test_closest_pairs.py` produces:
- 3 test cases demonstrating correctness
- Performance measurements for n=10,20,40,80,160 points
- Execution times showing O(n² log n) growth

## Algorithm Performance
- Time Complexity: O(n² log n)
- Space Complexity: O(n²)
```
