"""
Medium

Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

 

Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.


Example 2:

Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.
Example 3:

Input: k = 4, n = 1
Output: []
Explanation: There are no valid combinations.
Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.
 

Constraints:

2 <= k <= 9
1 <= n <= 60
"""

from typing import List


def combinationSum3(k: int, n: int) -> List[List[int]]:
    combinations = []  # Initialize the combinations list

    def dfs(start, combination, numbers_needed, remaining):
        # If the remaining is 0 and the numbers needed is 0, the combination is valid and add to the combinations list
        if remaining == 0 and numbers_needed == 0:
            combinations.append(combination)
            return
        # If the remaining is less than 0 or the numbers needed is less than 0, return because the combination is invalid
        if remaining < 0 or numbers_needed <= 0:
            return
        for num in range(start, 10):  # Iterate through the numbers from start to 9
            # Call the dfs function with the next number, and the updated combination, numbers needed, and remaining
            dfs(num + 1, combination + [num], numbers_needed - 1, remaining - num)

    # Start the dfs function with the first number, empty combination, k numbers needed, and n remaining target
    dfs(1, [], k, n)
    return combinations  # Return the combinations list


"""
Test Cases:
"""

k = 3
n = 7
assert sorted(combinationSum3(k, n)) == sorted([[1, 2, 4]])

k = 3
n = 9
assert sorted(combinationSum3(k, n)) == sorted([[1, 2, 6], [1, 3, 5], [2, 3, 4]])

k = 4
n = 1
assert sorted(combinationSum3(k, n)) == sorted([])

print("All test cases passed!")

"""
Time Complexity: O(9^k) because we have 9 choices for each of the k numbers
Space Complexity: O(k) because we store the combination
"""

# Previous: 40-combination-sum-ii.py
