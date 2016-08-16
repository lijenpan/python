"""
Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.
======================
Essentially the question is asking you to show if you understand what division is doing.
Q = N / D.
1. Align the most-significant bits of N and D.
2. Compute t = (N - D)
3. If t >= 0, then set the least significant bit of Q to 1, and set N = t.
4. Left-shift N by 1.
5. Left-shift Q by 1.
6. Go to step 2.

Alternatively, without using bitwise operation you can still do it by keep subtracting. But this is going to be
really slow in some cases.

I never find this to be any practical use in real world scenario. At least I never encounter one so far.
"""


def divide(dividend, divisor):
    """
    :type dividend: int
    :type divisor: int
    :rtype: int
    """
    INT_MAX = 2**31 - 1
    if divisor == 0:
        return INT_MAX
    neg = dividend > 0 and divisor < 0 or dividend < 0 and divisor > 0
    a, b = abs(dividend), abs(divisor)
    ans, shift = 0, 31
    while shift >= 0:
        if a >= b << shift:
            a -= b << shift
            ans += 1 << shift
        shift -= 1
    if neg:
        ans = - ans
    if ans > INT_MAX:
        return INT_MAX
    return ans
