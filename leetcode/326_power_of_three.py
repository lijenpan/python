"""
Given an integer, write a function to determine if it is a power of three.

Follow up:
Could you do it without using any loop / recursion?
==============================
To solve this problem without loop/recursion I would consider cheating.
"""


def isPowerOfThree(n):
    """
    :type n: int
    :rtype: bool
    """
    if n <= 0:
        return False
    while n % 3 == 0:
        n /= 3
    return n == 1
