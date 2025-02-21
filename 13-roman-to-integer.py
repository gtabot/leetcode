"""
Easy

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

 

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.


Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.


Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
"""


def romanToInt(s: str) -> int:
    value = 0  # Initialize the value to 0
    # Create a dictionary of values for the roman numerals
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    subtractions = {  # Create a dictionary of subtractions cases and their values
        "I": {"V": 4, "X": 9},
        "X": {"L": 40, "C": 90},
        "C": {"D": 400, "M": 900},
    }
    i = 0
    while i < len(s):
        ch = s[i]
        # If the current character is in the subtractions dictionary and the next character is a valid subtraction, add the subtraction value to the total
        if ch in subtractions and i + 1 < len(s) and s[i + 1] in subtractions[ch]:
            value += subtractions[ch][s[i + 1]]
            i += 2  # Increment the index by 2 to skip the next character
        else:
            value += values[ch]  # Add the value of the current character to the total
            i += 1  # Increment the index by 1
    return value


"""
Test cases
"""

s = "III"
assert romanToInt(s) == 3

s = "LVIII"
assert romanToInt(s) == 58

s = "MCMXCIV"
assert romanToInt(s) == 1994

print("All test cases passed!")

"""
Time complexity: O(n) where n is the length of the string
Space complexity: O(1) because all data structures used are fixed size regardless of the input size
"""

# Next: 12-integer-to-roman.py
