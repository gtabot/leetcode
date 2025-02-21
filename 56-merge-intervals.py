"""
Medium

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].


Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
"""

from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort()  # Sort intervals
    result = [intervals[0]]  # Initialize result with first interval
    for current in intervals[1:]:
        # If current interval does not overlap with last interval
        if current[0] > result[-1][1]:
            result.append(current)
        else:  # If current interval overlaps with last interval
            # Update last interval end time to max of end times of both intervals
            result[-1][1] = max(current[1], result[-1][1])
    return result


"""
Test Cases
"""

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
assert merge(intervals) == [[1, 6], [8, 10], [15, 18]]

intervals = [[1, 4], [4, 5]]
assert merge(intervals) == [[1, 5]]

print("All cases passed!")

"""
Time Complexity: O(n log n) because of sorting
Space Complexity: O(n) because of result array
"""

# Next: 57-insert-interval.py
