"""
Medium

Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

 

Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2


Example 2:

Input: intervals = [[7,10],[2,4]]
Output: 1
 

Constraints:

1 <= intervals.length <= 104
0 <= starti < endi <= 106
"""

from typing import List


def minMeetingRooms(intervals: List[List[int]]) -> int:
    max_rooms = 0
    rooms_needed = 0
    # Sort the starts and ends of the intervals
    starts = sorted([x[0] for x in intervals])
    ends = sorted([x[1] for x in intervals])
    s, e = 0, 0
    # Iterate through intervals between start and end times
    while s < len(intervals) and e < len(intervals):
        # If a start is before the next end, we need a new room
        if starts[s] < ends[e]:
            rooms_needed += 1
            max_rooms = max(rooms_needed, max_rooms)
            s += 1
        # If a start is after the next end, we can free up a room
        else:
            rooms_needed -= 1
            e += 1
    return max_rooms


"""
Test cases
"""

intervals = [[0, 30], [5, 10], [15, 20]]
assert minMeetingRooms(intervals) == 2

intervals = [[7, 10], [2, 4]]
assert minMeetingRooms(intervals) == 1

print("All test cases passed!")

"""
Time complexity: O(n log n) due to sorting
Space complexity: O(n) due to storing sorted starts and ends
"""

# Next: 2402-meeting-rooms-iii.py
