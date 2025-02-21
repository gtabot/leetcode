"""
Easy

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps


Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45
"""


def climbStairs(n: int) -> int:
    if n <= 2:  # Base case: if n <= 2, there are n ways to climb the stairs
        return n
    # Initialize an array to store the number of ways to climb the stairs
    ways = [0] * (n + 1)
    # There is 1 way to climb 1 step and 2 ways to climb 2 steps
    ways[1] = 1
    ways[2] = 2
    # Iterate over the stairs from 3 to n
    for k in range(3, len(ways)):
        # The number of ways to climb to the kth stair is the sum of the ways to climb the (k-1)th and (k-2)th stairs because you can get to the kth stair from either the (k-1)th or the (k-2)th stair
        ways[k] = ways[k - 1] + ways[k - 2]
    return ways[n]


"""
Test Cases
"""

n = 2
assert climbStairs(n) == 2

n = 3
assert climbStairs(n) == 3

print("All test cases passed!")

"""

Time Complexity: O(n) because we iterate through the stairs once
Space Complexity: O(n) because we use an array to store the number of ways to climb the stairs
"""

# TODO: Next: 2400-number-of-ways-to-reach-a-position-after-exactly-k-steps.py
# TODO: Next: 3154-find-number-of-ways-to-reach-the-k-th-stair.py
