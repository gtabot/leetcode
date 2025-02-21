"""
Medium

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""

from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    result = set()
    for idx, n in enumerate(nums):  # For each n, find pairs in remaining that equal -n
        two_sums = twoSumTarget(nums[idx + 1 :], -n)
        for p, q in two_sums:
            result.add((n, p, q))  # Add n and two sum pair to result
    return list(result)


def twoSumTarget(nums: List[int], target: int) -> List[List[int]]:
    result = []
    seen = {}
    for n in nums:
        if target - n in seen:
            result.append([target - n, n])
        seen[n] = True
    return result


"""
Test Cases
"""

nums = [-1, 0, 1, 2, -1, -4]
assert sorted(threeSum(nums)) == [(-1, -1, 2), (-1, 0, 1)]

nums = [0, 1, 1]
assert threeSum(nums) == []

nums = [0, 0, 0]
assert threeSum(nums) == [(0, 0, 0)]

print("All test cases passed!")


"""
Time Complexity: O(n^2) because we have a nested loop
Space Complexity: O(n) for the seen dictionary
"""

# Previous: 1-two-sum.py
# Next: 18-4sum.py
