"""
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
==============================
Anagram is same character set but re-arranged. So we just need to confirm each character count matches.
"""
from collections import Counter


def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s) != len(t):
        return False

    s_count = Counter(s)
    t_counter = Counter(t)

    for k, v in s_count.iteritems():
        if t_counter[k] != v:
            return False
    return True
