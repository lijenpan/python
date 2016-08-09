"""
Given a string, find the length of the longest substring without repeating characters.

Examples:
Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3.

Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


def length_of_longest_substring(s):
    """
    :type s: str
    :rtype: int
    """
    ans = 0
    left = 0
    last = {}
    for i in xrange(0, len(s)):
        if s[i] in last and last[s[i]] >= left:
            left = last[s[i]] + 1
        last[s[i]] = i
        ans = max(ans, i - left + 1)
    return ans


if __name__ == "__main__":
    assert length_of_longest_substring("abcabcbb") == 3
    assert length_of_longest_substring("bbbbb") == 1
    assert length_of_longest_substring("pwwkew") == 3
