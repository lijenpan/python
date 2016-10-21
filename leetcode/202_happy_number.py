"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
==============================
This question shouldn't be easy. The naive approach will get you stuck in the loop.
Until you found out that (through repetitions) happy numbers contains 4, you are in for
a hell of a coding session.
"""


def isHappy(n):
    """
    :type n: int
    :rtype: bool
    """
    temp = 0
    while n != 1 and n != 4:
        while n:
            temp += (n % 10) * (n % 10)
            n /= 10
        n = temp
        temp = 0
    return 1 == n
