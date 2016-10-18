"""
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.
==============================
Bit-wise operation. I never need to use this at work.
"""


def getSum(a, b):
    """
    :type a: int
    :type b: int
    :rtype: int
    """
    MIN_INT = 0x80000000
    MAX_INT = 0xffffffff
    for _ in xrange(32):
        a, b = a ^ b, (a & b) << 1
    return a if a & MIN_INT else a & MAX_INT
