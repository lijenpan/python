"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T
in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the empty string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.
==================================
I can't think of a solution without two pointers. I would not have come to this answer:
https://discuss.leetcode.com/topic/20692/12-lines-python
"""


def minWindow(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    min_start = 0
    min_end = len(s) - 1
    res = ''
    req = collections.defaultdict(int)
    obt = collections.defaultdict(int)
    for itr in t:
        req[itr] += 1
    l = i = j = 0
    while i < len(s):
        obt[s[i]] += 1
        if s[i] in req and obt[s[i]] <= req[s[i]]:
            l += 1
        if l == len(t):
            while l == len(t):
                obt[s[j]] -= 1
                if not req[s[j]] or obt[s[j]] >= req[s[j]]:
                    j += 1
                else:
                    if i - j <= min_end - min_start:
                        min_start = j
                        min_end = i
                        res = s[min_start:min_end + 1]
                    j += 1
                    l -= 1
        i += 1
    return res
