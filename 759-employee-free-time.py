"""
Hard

We are given a list schedule of employees, which represents the working time for each employee.

Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.

Return the list of finite intervals representing common, positive-length free time for all employees, also in sorted order.

(Even though we are representing Intervals in the form [x, y], the objects inside are Intervals, not lists or arrays. For example, schedule[0][0].start = 1, schedule[0][0].end = 2, and schedule[0][0][0] is not defined).  Also, we wouldn't include intervals like [5, 5] in our answer, as they have zero length.

 

Example 1:

Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
Output: [[3,4]]
Explanation: There are a total of three employees, and all common
free time intervals would be [-inf, 1], [3, 4], [10, inf].
We discard any intervals that contain inf as they aren't finite.


Example 2:

Input: schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
Output: [[5,6],[7,9]]
 

Constraints:

1 <= schedule.length , schedule[i].length <= 50
0 <= schedule[i].start < schedule[i].end <= 10^8
"""

from typing import List


class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end

    def __eq__(self, other):
        if not isinstance(other, Interval):
            return False
        return self.start == other.start and self.end == other.end


def employeeFreeTime(schedule: List[List[Interval]]) -> List[Interval]:
    free_time = []
    # Combine all intervals into a single list and sort them by start time
    combined_schedule = []
    for employee_schedule in schedule:
        for interval in employee_schedule:
            combined_schedule.append(interval)
    combined_schedule.sort(key=lambda x: x.start)
    # Initialize the previous end to the first interval's end
    prev_interval_end = combined_schedule[0].end
    for next_interval in combined_schedule[1:]:
        # If the current interval starts after the previous interval ends, there is a free time interval
        if next_interval.start > prev_interval_end:
            free_time.append(Interval(prev_interval_end, next_interval.start))
        # Update the previous end to the maximum of the current interval's end
        prev_interval_end = max(next_interval.end, prev_interval_end)
    return free_time


"""
Test Cases
"""
schedule = [
    [Interval(1, 2), Interval(5, 6)],
    [Interval(1, 3)],
    [Interval(4, 10)],
]
assert employeeFreeTime(schedule) == [Interval(3, 4)]

schedule = [
    [Interval(1, 3), Interval(6, 7)],
    [Interval(2, 4)],
    [Interval(2, 5), Interval(9, 12)],
]
assert employeeFreeTime(schedule) == [Interval(5, 6), Interval(7, 9)]

print("All test cases passed!")

"""
Time Complexity: O(n log n) because we sort the combined schedule
Space Complexity: O(n) because we create a new list to store the free time intervals
"""

# Previous: 2402-meeting-rooms-iii.py
