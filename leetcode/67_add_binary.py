"""
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
==================================
If you know Python pretty well, you just need one line of code.
"""


def addBinary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    # Beats 93.33% of Python submissions.
    return bin(int(a, 2) + int(b, 2)).replace('0b', '')
