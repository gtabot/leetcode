"""
Medium 

You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 109.

 

Example 1:


Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right


Example 2:


Input: obstacleGrid = [[0,1],[0,0]]
Output: 1
"""

from typing import List


def uniquePathsWithObstacles(obstacleGrid: List[List[int]]) -> int:
    m, n = len(obstacleGrid), len(obstacleGrid[0])  # Get the dimensions of the grid
    # Initialize a 2D array to store the number of unique paths to each cell
    unique_paths = [[0 for _ in range(n)] for _ in range(m)]
    # Initialize the top-left cell to 1 if there is no obstacle, otherwise 0
    unique_paths[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
    for r in range(m):  # Iterate through the grid
        for c in range(n):
            # Skip the top-left cell or any cells that are obstacles
            if (r == 0 and c == 0) or obstacleGrid[r][c] == 1:
                continue
            # The number of unique paths to the current cell is the sum of the unique paths to the cell above it and to the left of it
            unique_paths[r][c] = (unique_paths[r - 1][c] if r > 0 else 0) + (
                unique_paths[r][c - 1] if c > 0 else 0
            )
    # Return the number of unique paths to the bottom-right cell
    return unique_paths[-1][-1]


"""
Test Cases
"""

obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
assert uniquePathsWithObstacles(obstacleGrid) == 2

obstacleGrid = [[0, 1], [0, 0]]
assert uniquePathsWithObstacles(obstacleGrid) == 1

print("All test cases passed!")

"""
Time Complexity: O(m * n) because we iterate through the grid once
Space Complexity: O(m * n) because we use a 2D array to store the number of unique paths to each cell
"""

# Next: 980-unique-paths-iii.py
