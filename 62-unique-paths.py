"""
Medium

There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

 

Example 1:


Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
 

Constraints:

1 <= m, n <= 100
"""


def uniquePaths(m: int, n: int) -> int:
    # Initialize a 2D array to store the number of unique paths to each cell
    unique_paths = [[0 for _ in range(n)] for _ in range(m)]
    # Initialize the top-left cell to 1 because there is 1 unique path to it
    unique_paths[0][0] = 1
    for r in range(m):  # Iterate through the grid
        for c in range(n):
            if r == 0 and c == 0:  # Skip the top-left cell
                continue
            # The number of unique paths to the current cell is the sum of the unique paths to the cell above it and to the left of it
            unique_paths[r][c] = (
                (unique_paths[r - 1][c] if r > 0 else 0)
                + (unique_paths[r][c - 1] if c > 0 else 0)
            )
    # Return the number of unique paths to the bottom-right cell
    return unique_paths[-1][-1]


"""
Test Cases
"""


m = 3
n = 7
assert uniquePaths(m, n) == 28

m = 3
n = 2
assert uniquePaths(m, n) == 3

print("All test cases passed!")

"""
Time Complexity: O(m * n) because we iterate through the grid once
Space Complexity: O(m * n) because we use a 2D array to store the number of unique paths to each cell
"""

# Next: 63-unique-paths-ii.py
