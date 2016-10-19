"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.

Note: You may assume the string contain only lowercase letters.
==============================
It's quite easy in Python. But to get pass the Time Limit Exceeded problem, we need to bring in Counter.
"""

from collections import Counter

def firstUniqChar(s):
    """
    :type s: str
    :rtype: int
    """
    char_counts = Counter(s)

    for i, c in enumerate(s):
        if char_counts[c] == 1:
            return i

    return -1
