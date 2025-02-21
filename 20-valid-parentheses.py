"""
Easy

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true


Example 2:

Input: s = "()[]{}"

Output: true


Example 3:

Input: s = "(]"

Output: false


Example 4:

Input: s = "([])"

Output: true

 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""


def isValid(s: str) -> bool:
    stack = []
    for ch in s:
        # If the character is an opening bracket, push it onto the stack
        if ch in ["(", "[", "{"]:
            stack.append(ch)
        # If the stack is empty and the character is a closing bracket, return False
        elif len(stack) == 0:
            return False
        # If the character is a closing bracket, pop the last element and check if it is the corresponding opening bracket,
        # if not, return False
        elif ch == ")":
            if stack.pop() != "(":
                return False
        elif ch == "]":
            if stack.pop() != "[":
                return False
        elif ch == "}":
            if stack.pop() != "{":
                return False
    return len(stack) == 0  # If the stack is empty, the string is valid


"""
Test cases
"""

s = "()"
assert isValid(s) == True

s = "()[]{}"
assert isValid(s) == True

s = "(]"
assert isValid(s) == False

s = "([])"
assert isValid(s) == True

print("All test cases passed")

"""
Time Complexity: O(n) because we iterate through the string once
Space Complexity: O(n) because we use a stack to store the characters
"""

# TODO: Next: 301-remove-invalid-parentheses.py
