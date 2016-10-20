"""
Given two non-negative numbers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
==============================
Loop whole: You can parse individual integer and compute carry-over. This is how you add big ints.
"""


def addStrings(num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """
    result = []
    carry = 0
    idx1, idx2 = len(num1), len(num2)
    while idx1 or idx2 or carry:
        digit = carry
        if idx1:
            idx1 -= 1
            digit += int(num1[idx1])
        if idx2:
            idx2 -= 1
            digit += int(num2[idx2])
        carry = digit > 9
        result.append(str(digit % 10))
    return ''.join(result[::-1])
