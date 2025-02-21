"""
Medium

Seven different symbols represent Roman numerals with the following values:

Symbol	Value
I	1
V	5
X	10
L	50
C	100
D	500
M	1000
Roman numerals are formed by appending the conversions of decimal place values from highest to lowest. Converting a decimal place value into a Roman numeral has the following rules:

If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input, append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral.
If the value starts with 4 or 9 use the subtractive form representing one symbol subtracted from the following symbol, for example, 4 is 1 (I) less than 5 (V): IV and 9 is 1 (I) less than 10 (X): IX. Only the following subtractive forms are used: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) and 900 (CM).
Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times to represent multiples of 10. You cannot append 5 (V), 50 (L), or 500 (D) multiple times. If you need to append a symbol 4 times use the subtractive form.
Given an integer, convert it to a Roman numeral.

 

Example 1:

Input: num = 3749

Output: "MMMDCCXLIX"

Explanation:

3000 = MMM as 1000 (M) + 1000 (M) + 1000 (M)
 700 = DCC as 500 (D) + 100 (C) + 100 (C)
  40 = XL as 10 (X) less of 50 (L)
   9 = IX as 1 (I) less of 10 (X)
Note: 49 is not 1 (I) less of 50 (L) because the conversion is based on decimal places


Example 2:

Input: num = 58

Output: "LVIII"

Explanation:

50 = L
 8 = VIII

 
 Example 3:

Input: num = 1994

Output: "MCMXCIV"

Explanation:

1000 = M
 900 = CM
  90 = XC
   4 = IV
"""


def intToRoman(num: int) -> str:
    # Create a mapping of values to Roman numerals
    value_to_roman = {1000: "M", 500: "D", 100: "C", 50: "L", 10: "X", 5: "V", 1: "I"}
    roman = ""
    place = 1  # Initialize the place value to 1
    # Iterate over the digits of the number by dividing by 10 until it is 0
    while num > 0:
        last_digit = num % 10  # Get the last digit of the number
        # If the last digit is 9, prepend the Roman numeral for {9 * place}, i.e. IX or CM
        if last_digit == 9:
            roman = value_to_roman[place] + value_to_roman[place * 10] + roman
        # If the last digit is greater than or equal to 5, prepend the Roman numeral for the {last digit * place}, i.e. V, VII or DCCC
        elif last_digit >= 5:
            roman = (
                value_to_roman[place * 5]
                + value_to_roman[place] * (last_digit - 5)
                + roman
            )
        # If the last digit is 4, prepend the Roman numeral for {4 * place}, i.e. IV or CD
        elif last_digit == 4:
            roman = value_to_roman[place] + value_to_roman[place * 5] + roman
        else:  # Otherwise, prepend the Roman numeral for the {last digit * place}, i.e. I or CCC
            roman = value_to_roman[place] * last_digit + roman
        num //= 10  # Truncate the last digit from the number
        place *= 10  # Increment the place value
    return roman


"""
Test cases
"""

num = 3749
assert intToRoman(num) == "MMMDCCXLIX"

num = 58
assert intToRoman(num) == "LVIII"

num = 1994
assert intToRoman(num) == "MCMXCIV"

print("All test cases passed!")


"""
Time Complexity: O(n) where n is the number of digits in the input number
Space Complexity: O(1) because we are not using any extra space as a function of the input size
"""

# Previous: 13-roman-to-integer.py
# TODO: Next: 273-integer-to-english-words.py
