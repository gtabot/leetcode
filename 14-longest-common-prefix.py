"""
Easy

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.
"""

from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    # Initialize prefix as an empty list to avoid multiple string concatenations
    prefix = []
    # Iterate through the characters of the shortest string
    for i in range(min(len(s) for s in strs)):
        # Check if all strings have the same character at the current index
        if not all(s[i] == strs[0][i] for s in strs):
            break
        prefix.append(strs[0][i])  # Append the character to the prefix
    return "".join(prefix)  # Return the joined prefix list as a string


"""
Test cases
"""

strs = ["flower", "flow", "flight"]
assert longestCommonPrefix(strs) == "fl"

strs = ["dog", "racecar", "car"]
assert longestCommonPrefix(strs) == ""

print("All test cases passed")

"""
Time complexity: O(n) where n is the length of the shortest string
Space complexity: O(s) where s is the length of the prefix
"""

# Next: 3460-longest-common-prefix-after-at-most-one-removal.py
