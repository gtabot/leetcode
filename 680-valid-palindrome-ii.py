"""
Easy

Given a string s, return true if the s can be palindrome after deleting at most one character from it.

 

Example 1:

Input: s = "aba"
Output: true


Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.


Example 3:

Input: s = "abc"
Output: false
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
"""


def is_palindrome(s: str) -> bool:
    def is_valid_with_deletion(l: int, r: int, can_delete: bool) -> bool:
        if not can_delete:  # If we can't delete, check if the string is a palindrome
            s_ = s[l : r + 1]
            return s_ == s_[::-1]
        while l < r:  # If we can delete, iterate through the string
            # If the characters are not the same, try deleting one of them
            if s[l] != s[r]:
                return (
                    is_valid_with_deletion(l + 1, r, False)
                    or is_valid_with_deletion(l, r - 1, False)
                )
            l, r = l + 1, r - 1  # Update the pointers
        return True  # If we didn't delete, the string is a palindrome

    # Check if the string is a palindrome, then check if we can delete one character to make it a palindrome
    return s == s[::-1] or is_valid_with_deletion(0, len(s) - 1, True)


"""
Test Cases
"""

assert is_palindrome("aba") == True
assert is_palindrome("abca") == True
assert is_palindrome("abc") == False

print("All test cases passed!")

"""
Time Complexity: O(n) because we iterate through the string once
Space Complexity: O(1) because we are not using any extra space
"""

# Previous: 9-palindrome-number.py