"""
'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
=====================================
This problem would be hard because you are essentially writing regexp function. But since there are no constraints
this is simple.
"""
import re


def isMatch(s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    return re.match(p + '$', s) != None
