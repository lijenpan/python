"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example,
Given s = "Hello World",
return 5.
==================================
You can't simply do s.split(' ') because there can be no words after the last whitespace.
And there are too many edge cases to make it work with indexing parsing. Just use regex.
"""

import re


def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    s = s.strip()
    result = re.findall(r'[a-zA-Z]+', s)
    if not result:
        return 0
    return len(result[-1])
