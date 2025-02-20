"""
Easy

Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.

 

Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: false


Example 2:

Input: intervals = [[7,10],[2,4]]
Output: true
 

Constraints:

0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti < endi <= 106
"""

from typing import List


def canAttendMeetings(intervals: List[List[int]]) -> bool:
    intervals.sort()
    # Iterate through the pairs of intervals
    for i in range(len(intervals) - 1):
        # There's a conflict if the end of the current meeting is greater than the start of the next meeting
        if intervals[i][1] > intervals[i + 1][0]:
            return False
    return True


"""
Test Cases
"""

intervals = [[0, 30], [5, 10], [15, 20]]
assert canAttendMeetings(intervals) == False

intervals = [[7, 10], [2, 4]]
assert canAttendMeetings(intervals) == True

print("All cases passed!")

"""
Time Complexity: O(n log n) because we sort the intervals
Space Complexity: O(1) because we don't use any extra space
"""

# Next: 253-meeting-rooms-ii.py
