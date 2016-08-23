"""
Implement int sqrt(int x).

Compute and return the square root of x.
==================================
Let's not cheat here.

This problem needs to solved by approximation. https://github.com/lijenpan/python/tree/master/netsuite
"""


def mySqrt(x, epsilon=0.000001):
    """
    :type x: int
    :rtype: int
    """
    if x < epsilon:
        return 0
    a = 1.5
    while True:
        if abs(a * a - x) < epsilon:
            return int(a)
        y = x / a
        a = (a + y) / 2
