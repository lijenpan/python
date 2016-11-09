"""
Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not
share common letters. You may assume that each word will contain only lower case letters. If no such two words exist,
return 0.

Example 1:
Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
Return 16
The two words can be "abcw", "xtfn".

Example 2:
Given ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
Return 4
The two words can be "ab", "cd".

Example 3:
Given ["a", "aa", "aaa", "aaaa"]
Return 0
No such pair of words.
===============================
Of course brute force will get you TLE. This guy has a clever way to keying words:
https://discuss.leetcode.com/topic/46685/python-solution-beats-99-67/2
"""


def maxProduct(words):
    """
    :type words: List[str]
    :rtype: int
    """
    d = {}
    for w in words:
        mask = 0
        for c in set(w):
            mask |= (1 << (ord(c) - 97))
        d[mask] = max(d.get(mask, 0), len(w))
    return max([d[x] * d[y] for x in d for y in d if not x & y] or [0])
