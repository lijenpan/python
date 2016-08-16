"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
==================================
This is a classic stack problem. In Python, this is really easy because list is stack.
"""


def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    stack = []
    for p in s:
        if p in ('(', '[', '{'):
            stack.append(p)
        else:
            if not stack:
                return False
            if (p == ']' and stack[-1] != '[') or (p == ')' and stack[-1] != '(') or (p == '}' and stack[-1] != '{'):
                return False
            stack.pop()
    return not stack
