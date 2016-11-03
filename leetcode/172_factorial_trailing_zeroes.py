"""
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.
==============================
The naive approach would be just compute the factorial and then count 0s.
But for a 0 to appear, there must be a 5. So every time the number is divisible by 5 there is a 0.
"""


def trailingZeroes(n):
    """
    :type n: int
    :rtype: int
    """
    return 0 if n == 0 else n / 5 + trailingZeroes(n / 5)
