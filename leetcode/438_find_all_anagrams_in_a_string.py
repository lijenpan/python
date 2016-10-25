"""
iven a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
==============================
Is this really easy? The naive approach with substrings will get TLE even with Counter.
So instead of substrings, we directly compare Counters.
"""
from collections import Counter


def findAnagrams(s, p):
    """
    :type s: str
    :type p: str
    :rtype: List[int]
    """
    res = []
    p_counter = Counter(p)
    s_counter = Counter(s[:len(p) - 1])
    for i in xrange(len(p) - 1, len(s)):
        s_counter[s[i]] += 1  # include a new char in the window
        if s_counter == p_counter:
            res.append(i - len(p) + 1)  # append the starting index
        s_counter[s[i - len(p) + 1]] -= 1  # decrease the count of oldest char in the window
        if s_counter[s[i - len(p) + 1]] == 0:
            del s_counter[s[i - len(p) + 1]]  # remove the count if it is 0
    return res
