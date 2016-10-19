"""
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
==============================
Not sure why this is categorized as easy, it's hard to get it right all the way. Some people even tried to solve this
using DP but you will probably run out of memory.

We can think of the problem this way. For a character can be used in palindrome it need at least 2, so we can find
which characters are left after pairing and use one of them for the palindrome center. The code is easy but arriving
at this solution, not so easy.
"""


def longestPalindrome(s):
    a = set()
    for x in s:
        if x in a:
            a.remove(x)
        else:
            a.add(x)
    return len(s) - len(a) if not a else len(s) - len(a) + 1
