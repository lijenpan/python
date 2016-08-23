"""
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.
==================================
Let's get creative.
"""


def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    digits = ''.join(map(str, digits))
    digits = int(digits)
    digits += 1
    return [int(d) for d in str(digits)]
