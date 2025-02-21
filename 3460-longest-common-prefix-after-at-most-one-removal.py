"""
Medium

You are given two strings s and t.

Return the length of the longest common prefix between s and t after removing at most one character from s.

Note: s can be left without any removal.

 

Example 1:

Input: s = "madxa", t = "madam"

Output: 4

Explanation:

Removing s[3] from s results in "mada", which has a longest common prefix of length 4 with t.

Example 2:

Input: s = "leetcode", t = "eetcode"

Output: 7

Explanation:

Removing s[0] from s results in "eetcode", which matches t.

Example 3:

Input: s = "one", t = "one"

Output: 3

Explanation:

No removal is needed.

Example 4:

Input: s = "a", t = "b"

Output: 0

Explanation:

s and t cannot have a common prefix.

 

Constraints:

1 <= s.length <= 105
1 <= t.length <= 105
s and t contain only lowercase English letters.
"""


def longestCommonPrefix(s: str, t: str, removed: bool = False) -> int:
    length = 0
    # Iterate for the length of the shortest string
    for i in range(min(len(s), len(t))):
        if s[i] != t[i]:  # If the characters are not the same...
            # ...and we have already removed a character, return the current length
            if removed:
                return length
            # ...or try removing a character from s and add count from there
            return length + longestCommonPrefix(s[i + 1 :], t[i:], removed=True)
        length += 1  # The characters are the same, so we can increment the length
    return length


s = "madxa"
t = "madam"
assert longestCommonPrefix(s, t) == 4

s = "leetcode"
t = "eetcode"
assert longestCommonPrefix(s, t) == 7

s = "one"
t = "one"
assert longestCommonPrefix(s, t) == 3

s = "a"
t = "b"
assert longestCommonPrefix(s, t) == 0

print("All test cases passed")

"""
Time Complexity: O(n) where n is the length of the shortest string
Space Complexity: O(1) because we are not using any extra space
"""

# Previous: 14-longest-common-prefix.py
