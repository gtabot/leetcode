"""
Medium

You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.

The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].

 

Example 1:


Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]


Example 2:

Input: firstList = [[1,3],[5,9]], secondList = []
Output: []
 

Constraints:

0 <= firstList.length, secondList.length <= 1000
firstList.length + secondList.length >= 1
0 <= starti < endi <= 109
endi < starti+1
0 <= startj < endj <= 109 
endj < startj+1
"""

from typing import List


def intervalIntersection(
    firstList: List[List[int]], secondList: List[List[int]]
) -> List[List[int]]:
    result = []
    i, j = 0, 0  # Pointers for firstList and secondList
    # Iterate through both lists
    while i < len(firstList) and j < len(secondList):
        max_start = max(firstList[i][0], secondList[j][0])
        min_end = min(firstList[i][1], secondList[j][1])
        # An intersection occurs if a start is before an end
        if max_start <= min_end:
            result.append([max_start, min_end])
        # Move pointer of list that ends first
        if firstList[i][1] <= secondList[j][1]:
            i += 1
        else:
            j += 1
    return result


"""
Test Cases
"""

firstList = [[0, 2], [5, 10], [13, 23], [24, 25]]
secondList = [[1, 5], [8, 12], [15, 24], [25, 26]]
assert intervalIntersection(firstList, secondList) == [
    [1, 2],
    [5, 5],
    [8, 10],
    [15, 23],
    [24, 24],
    [25, 25],
]

firstList = [[1, 3], [5, 9]]
secondList = []
assert intervalIntersection(firstList, secondList) == []

print("All cases passed!")

"""
Time Complexity: O(n + m) because we iterate through both lists
Space Complexity: O(n + m) because we create a new result array and in the worst case, we add all intervals to the result
"""
