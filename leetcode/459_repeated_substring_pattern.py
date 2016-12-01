"""
Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of
the substring together. You may assume the given string consists of lowercase English letters only and its length
will not exceed 10000.

Example 1:
Input: "abab"

Output: True

Explanation: It's the substring "ab" twice.
Example 2:
Input: "aba"

Output: False
Example 3:
Input: "abcabcabcabc"

Output: True

Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
===============================
I would just keep trying substrings. But here is an amazing solution:
https://discuss.leetcode.com/topic/68206/easy-python-solution-with-explaination/2
"""


def repeatedSubstringPattern(str):
    """
    :type str: str
    :rtype: bool
    """
    return str in (2 * str)[1:-1]
