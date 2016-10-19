"""
Given an integer, write a function to determine if it is a power of two.
==============================
You don't want to keep subtracting 2.
"""


def isPowerOfTwo(n):
    """
    :type n: int
    :rtype: bool
    """
    return bin(n).count('1') == 1 if n > 0 else False
