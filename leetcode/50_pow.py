"""
Implement pow(x, n).
==================================
What's wrong with x**n?? Guess I'm missing the point...

Oh n can be negative!

This is considered not fast enough:
def myPow(x, n):
    if n == 0:
        return 1.0
    total = 1.0
    for _ in xrange(0, abs(n)):
        total *= x
    if n < 0:
        total = 1.0 / total
    return total

Turns out some smartass came up with x^n = x^(n/2) * x^(n/2) * x^(n%2). Fancy that!
"""


def myPow(x, n):
    """
    :type x: float
    :type n: int
    :rtype: float
    """
    if n == 0:
        return 1.0
    elif n < 0:
        return 1 / myPow(x, -n)
    elif n % 2:
        return myPow(x * x, n / 2) * x
    else:
        return myPow(x * x, n / 2)
