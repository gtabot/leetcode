"""
Hard

You are given an m x n integer array grid where grid[i][j] could be:

1 representing the starting square. There is exactly one starting square.
2 representing the ending square. There is exactly one ending square.
0 representing empty squares we can walk over.
-1 representing obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.

 

Example 1:


Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)


Example 2:


Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
Output: 4
Explanation: We have the following four paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)


Example 3:


Input: grid = [[0,1],[2,0]]
Output: 0
Explanation: There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 20
1 <= m * n <= 20
-1 <= grid[i][j] <= 2
There is exactly one starting cell and one ending cell.
"""

from copy import deepcopy
from typing import List


def uniquePathsIII(grid_: List[List[int]]) -> int:
    # Deep copy the grid to avoid modifying the original grid
    grid = deepcopy(grid_)
    # Get the dimensions of the grid
    m, n = len(grid), len(grid[0])
    # Find the starting cell and count the number of empty squares
    start_x, start_y, empty_squares = None, None, 0
    for r in range(m):
        for c in range(n):
            if grid[r][c] == 1:
                start_x, start_y = r, c
            if grid[r][c] != -1:
                empty_squares += 1
    # If the starting cell is not found, return 0
    if start_x is None or start_y is None:
        return 0

    # Define a helper function to perform a depth-first search with backtracking
    def dfs(x, y, empty_squares):
        # If the current cell is out of bounds or an obstacle, return 0
        if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == -1:
            return 0
        empty_squares -= 1  # The current cell is an empty square so decrement the count
        # If the current cell is the ending cell, return 1 if all empty squares have been visited, otherwise return 0
        if grid[x][y] == 2:
            return 1 if empty_squares == 0 else 0
        grid[x][y] = -1  # Mark the current cell as visited
        paths = (  # Recursively explore all possible paths
            dfs(x + 1, y, empty_squares)
            + dfs(x - 1, y, empty_squares)
            + dfs(x, y + 1, empty_squares)
            + dfs(x, y - 1, empty_squares)
        )
        grid[x][y] = 0  # Mark the current cell as unvisited for backtracking
        return paths  # Return the total number of paths found from the current cell

    # Start the depth-first search from the starting cell with the count of empty squares
    return dfs(start_x, start_y, empty_squares)


"""
Test Cases
"""

grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]
print(uniquePathsIII(grid))
assert uniquePathsIII(grid) == 2

grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]
assert uniquePathsIII(grid) == 4

grid = [[0, 1], [2, 0]]
assert uniquePathsIII(grid) == 0

print("All test cases passed!")

"""
Time Complexity: O(m * n) because we iterate through the grid
Space Complexity: O(m * n) because we use a deep copy of the grid
"""

# Prev: 63-unique-paths-ii.py
