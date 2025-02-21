"""
Easy

Given an array of integers arr, replace each element with its rank.

The rank represents how large the element is. The rank has the following rules:

Rank is an integer starting from 1.
The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
Rank should be as small as possible.
 

Example 1:

Input: arr = [40,10,20,30]
Output: [4,1,2,3]
Explanation: 40 is the largest element. 10 is the smallest. 20 is the second smallest. 30 is the third smallest.

Example 2:

Input: arr = [100,100,100]
Output: [1,1,1]
Explanation: Same elements share the same rank.
Example 3:

Input: arr = [37,12,28,9,100,56,80,5,12]
Output: [5,3,4,2,8,6,7,1,3]
 

Constraints:

0 <= arr.length <= 10^5
-10^9 <= arr[i] <= 10^9
"""

from typing import List


def arrayRankTransform(arr: List[int]) -> List[int]:
    sorted_unique = sorted(set(arr))  # Sort the unique elements
    # Create a dictionary to store the rank of each element
    rank = {x: rank for rank, x in enumerate(sorted_unique, start=1)}
    return [rank[x] for x in arr]  # Replace each element with its rank


"""
Test Cases
"""

arr = [40, 10, 20, 30]
assert arrayRankTransform(arr) == [4, 1, 2, 3]

arr = [100, 100, 100]
assert arrayRankTransform(arr) == [1, 1, 1]

arr = [37, 12, 28, 9, 100, 56, 80, 5, 12]
assert arrayRankTransform(arr) == [5, 3, 4, 2, 8, 6, 7, 1, 3]

print("All test cases passed!")


"""
Time Complexity: O(n log n) because we sort the array
Space Complexity: O(n) because we create a dictionary to store the rank of each element
"""

# TODO: Next: 1632-rank-transform-of-a-matrix.py
