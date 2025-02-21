"""
Medium

Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]


Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
 

Constraints:

1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
"""

from typing import List


def fourSum(nums: List[int], target: int) -> List[List[int]]:
    # Use recursive kSum function to find all unique quadruplets
    return kSum(4, nums, target)


def kSum(k, nums: List[int], target: int) -> List[List[int]]:
    nums.sort()  # Sort the array to make it easier to find duplicates
    if k == 2:  # Base case: if k is 2, use twoSum function
        return twoSum(nums, target)
    result = set()  # Store results in a set to avoid duplicates
    for idx, n in enumerate(nums):
        # Recursively call kSum with k-1, nums[idx + 1 :], and target - n
        tuples = kSum(k - 1, nums[idx + 1 :], target - n)
        for tup in tuples:  # Combine n with the tuples returned by kSum
            result.add((n,) + tup)
    return list(result)


def twoSum(nums: List[int], target: int) -> List[List[int]]:
    result = set()
    seen = {}
    for n in nums:
        if target - n in seen:
            result.add((target - n, n))
        seen[n] = True
    return list(result)


"""
Test Cases
"""

nums = [1, 0, -1, 0, -2, 2]
target = 0
assert sorted(fourSum(nums, target)) == [(-2, -1, 1, 2), (-2, 0, 0, 2), (-1, 0, 0, 1)]

nums = [2, 2, 2, 2, 2]
target = 8
assert fourSum(nums, target) == [(2, 2, 2, 2)]

print("All test cases passed!")


"""
Time Complexity: O(n^3) because we have nested loops and a two sum function
Space Complexity: O(n) because we are using a set to store the result and the seen dictionary
"""
