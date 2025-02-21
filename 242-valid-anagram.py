"""
Easy

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true


Example 2:

Input: s = "rat", t = "car"

Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""

from collections import Counter


def isAnagram(s: str, t: str) -> bool:
    # If the strings are not the same length, they cannot be anagrams
    if len(s) != len(t):
        return False
    # If the strings have the same frequency of characters, they are anagrams
    return Counter(s) == Counter(t)


"""
Test cases
"""

s = "anagram"
t = "nagaram"
assert isAnagram(s, t) == True

s = "rat"
t = "car"
assert isAnagram(s, t) == False

"""
Time Complexity: O(n) because we iterate through the strings once
Space Complexity: O(n) because we use a Counter to store the frequency of each character
"""
