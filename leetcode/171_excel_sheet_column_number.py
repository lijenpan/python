"""
Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
==============================
If you think about using mapping column to index, you will have hard time to get this to work.
"""


def titleToNumber(s):
    """
    :type s: str
    :rtype: int
    """
    res = 0
    for c in s:
        res = res * 26 + ord(c) - ord('A') + 1
    return res
