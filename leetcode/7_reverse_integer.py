"""
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321
====================================
You shouldn't need to take out the big gun (e.g. bitwise operation) to solve this issue.
Revert string works just fine without overflows.
"""


def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    if x < 0:
        sign = -1
    else:
        sign = 1
    x_str = str(abs(x))
    r = x_str[::-1]
    return sign * int(r)


if __name__ == "__main__":
    assert reverse(123) == 321
    assert reverse(-123) == -321
    assert reverse(1000000003) == 3000000001
