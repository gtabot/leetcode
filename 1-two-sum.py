"""
Easy

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
"""

from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    # Create a dictionary to store the numbers and their indices
    num_to_index = {}
    for idx, num in enumerate(nums):
        # If the complement of the current number is in the dictionary, return the indices
        if target - num in num_to_index:
            return [num_to_index[target - num], idx]
        # Add the current number and its index to the dictionary
        num_to_index[num] = idx
    return []


"""
Test Cases
"""

nums = [2, 7, 11, 15]
target = 9
assert two_sum(nums, target) == [0, 1]

nums = [3, 2, 4]
target = 6
assert two_sum(nums, target) == [1, 2]

nums = [3, 3]
target = 6
assert two_sum(nums, target) == [0, 1]

print("All test cases passed!")


"""
Time Complexity: O(n) because we iterate through the list once
Space Complexity: O(n) because we use a dictionary to store the numbers and their indices
"""

# Next: 15-3sum.py
