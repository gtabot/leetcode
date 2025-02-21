"""
Easy

You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

 

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r


Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s


Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
 

Constraints:

1 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.
"""


def mergeAlternately(word1: str, word2: str) -> str:
    # Initialize the result as a list to avoid inneficient string concatenation
    result = []
    # Zip the two strings and iterate over the pairs while tracking the index
    for i, (a, b) in enumerate(zip(word1, word2)):
        result.extend([a, b])  # Extend the result with each string's character
    # Return the result with any remaining characters from the longer string
    return "".join(result) + word1[i + 1 :] + word2[i + 1 :]


"""
Test cases
"""

word1 = "abc"
word2 = "pqr"
assert mergeAlternately(word1, word2) == "apbqcr"

word1 = "ab"
word2 = "pqrs"
assert mergeAlternately(word1, word2) == "apbqrs"

word1 = "abcd"
word2 = "pq"
assert mergeAlternately(word1, word2) == "apbqcd"

print("All test cases passed")

"""
Time complexity: O(n) where n is the length of the longer string
Space complexity: O(1) because we are not using any extra space
"""

# TODO: Next: 281-zigzag-iterator.py
