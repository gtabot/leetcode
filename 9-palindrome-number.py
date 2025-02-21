"""
Easy

Given an integer x, return true if x is a palindrome, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.


Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
 

Follow up: Could you solve it without converting the integer to a string?
"""


def is_palindrome(x: int) -> bool:
    # Negative numbers and numbers ending in 0 are not palindromes
    if x < 0 or (x != 0 and x % 10 == 0):
        return False
    s = str(x)  # Convert the integer to a string
    return s == s[::-1]  # Return if the string is equal to its reverse


def is_palindrome_without_string(x: int) -> bool:
    # Negative numbers and numbers ending in 0 are not palindromes
    if x < 0 or (x != 0 and x % 10 == 0):
        return False
    x_ = x  # Make a copy of the number
    reversed = 0  # Initialize the reversed number
    while x_ > 0:  # While the copy is greater than 0
        digit = x_ % 10  # Get the last digit
        reversed = reversed * 10 + digit  # Add the digit to the reversed number
        x_ //= 10  # Remove the last digit from the copy
    return x == reversed  # Return if the number is equal to its reverse


"""
Test Cases
"""

assert is_palindrome(121) == True
assert is_palindrome(-121) == False
assert is_palindrome(10) == False

assert is_palindrome_without_string(121) == True
assert is_palindrome_without_string(-121) == False
assert is_palindrome_without_string(10) == False

print("All test cases passed!")

"""
Time Complexity: O(n) where n is the number of digits in the number
Space Complexity: O(1) because we are only storing a few variables
"""

# Previous: 125-valid-palindrome.py
# Next: 680-valid-palindrome-ii.py
