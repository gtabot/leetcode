"""
Easy

A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their lengths. The lengths should not have leading zeros.

For example, a string such as "substitution" could be abbreviated as (but not limited to):

"s10n" ("s ubstitutio n")
"sub4u4" ("sub stit u tion")
"12" ("substitution")
"su3i1u2on" ("su bst i t u ti on")
"substitution" (no substrings replaced)
The following are not valid abbreviations:

"s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
"s010n" (has leading zeros)
"s0ubstitution" (replaces an empty substring)
Given a string word and an abbreviation abbr, return whether the string matches the given abbreviation.

A substring is a contiguous non-empty sequence of characters within a string.

 

Example 1:

Input: word = "internationalization", abbr = "i12iz4n"
Output: true
Explanation: The word "internationalization" can be abbreviated as "i12iz4n" ("i nternational iz atio n").


Example 2:

Input: word = "apple", abbr = "a2e"
Output: false
Explanation: The word "apple" cannot be abbreviated as "a2e".
 

Constraints:

1 <= word.length <= 20
word consists of only lowercase English letters.
1 <= abbr.length <= 10
abbr consists of lowercase English letters and digits.
All the integers in abbr will fit in a 32-bit integer.
"""


def validWordAbbreviation(word: str, abbr: str) -> bool:
    # Two pointers to iterate through the word and the abbreviation
    w, a = 0, 0
    while w < len(word) and a < len(abbr):
        if abbr[a].isalpha():  # If the current abbreviation character is a letter
            if word[w] != abbr[a]:  # If the characters are not the same, return False
                return False
            w, a = w + 1, a + 1  # Increment both pointers
        elif abbr[a].isnumeric():  # If the current abbreviation character is a number
            if abbr[a] == "0":  # If the number has a leading zero, return False
                return False
            num = int(abbr[a])  # Convert the number to an integer
            a += 1  # Increment the abbreviation pointer
            # While the next character exists and is a digit, update the number
            while a < len(abbr) and abbr[a].isdigit():
                num = 10 * num + int(abbr[a])
                a += 1  # Increment the abbreviation pointer
            w += num  # Increment the word pointer by the number
    # Return True if the word and abbreviation pointers have reached the end of the string
    return w == len(word) and a == len(abbr)


word = "internationalization"
abbr = "i12iz4n"
assert validWordAbbreviation(word, abbr) == True


word = "apple"
abbr = "a2e"
assert validWordAbbreviation(word, abbr) == False


print("All test cases passed")
