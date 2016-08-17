"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed)
parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
==================================
Built on top of Q20. But tracking index and compute length instead.
"""


def longestValidParentheses(s):
    """
    :type s: str
    :rtype: int
    """
    stack = [-1]
    max_length = 0
    for i in xrange(len(s)):
        if s[i] == ')' and stack[-1] != -1 and s[stack[-1]] == '(':
            stack.pop()
            max_length = max(max_length, i - stack[-1])
        else:
            stack.append(i)
    return max_length
