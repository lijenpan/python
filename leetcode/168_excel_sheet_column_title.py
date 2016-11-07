"""
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
===============================

"""


def convertToTitle(n):
    """
    :type n: int
    :rtype: str
    """
    res = ''
    while n > 0:
        res += chr(ord('A') + (n - 1) % 26)
        n = (n - 1) / 26
    return res[::-1]
