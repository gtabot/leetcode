"""
Easy

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""


def is_palindrome(s: str) -> bool:
    # Convert all uppercase letters to lowercase and remove non-alphanumeric characters
    s = [ch.lower() for ch in s if ch.isalnum()]
    return s == s[::-1]  # Return if the string is equal to its reverse


"""
Test Cases
"""

assert is_palindrome("A man, a plan, a canal: Panama") == True
assert is_palindrome("race a car") == False
assert is_palindrome(" ") == True

print("All test cases passed!")

"""
Time Complexity: O(n) where n is the number of characters in the string
Space Complexity: O(n) where n is the number of characters in the string
"""

# Next: 9-palindrome-number.py
