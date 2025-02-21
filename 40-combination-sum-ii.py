"""
Medium

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

 

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]


Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
 

Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
"""


def combinationSum2(candidates, target):
    combinations = []  # Initialize the combinations list
    candidates.sort()  # Sort the candidates to easily avoid duplicates

    def backtrack(idx, combination, remaining):
        # If the remaining is 0, the combination is valid and add to the combinations list
        if remaining == 0:
            combinations.append(combination[:])
            return
        # Iterate through the candidates starting from the current index
        for i in range(idx, len(candidates)):
            # If the current candidate is the same as the previous candidate, skip it to avoid duplicates
            if i > idx and candidates[i] == candidates[i - 1]:
                continue
            # If the remaining is less than the current candidate, break because the candidates are sorted
            if remaining - candidates[i] < 0:
                break
            # Add the current candidate to the combination and recursively call the backtrack function
            backtrack(i + 1, combination + [candidates[i]], remaining - candidates[i])

    # Start the backtracking process with the first index, empty combination, and the target
    backtrack(0, [], target)
    return combinations  # Return the combinations list


"""
Test Cases:
"""

candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
assert sorted(combinationSum2(candidates, target)) == sorted(
    [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
)

candidates = [2, 5, 2, 1, 2]
target = 5
assert sorted(combinationSum2(candidates, target)) == sorted([[1, 2, 2], [5]])

print("All test cases passed!")

"""
Time Complexity: O(n * 2^n) because we have n choices for each of the 2^n combinations
Space Complexity: O(n) because we store the combination
"""

# Previous: 39-combination-sum.py
# Next: 216-combination-sum-iii.py
