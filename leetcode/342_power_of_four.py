"""
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example:
Given num = 16, return true. Given num = 5, return false.

Follow up: Could you solve it without loops/recursion?
==============================
I don't like magic number.
"""


def isPowerOfFour(n):
    """
    :type n: int
    :rtype: bool
    """
    if n <= 0:
        return False
    while n % 4 == 0:
        n /= 4
    return n == 1
