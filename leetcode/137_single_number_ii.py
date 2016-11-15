"""
Given an array of integers, every element appears three times except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
===============================
I really don't like bit manipulation.
"""


def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    a = set(nums)
    a = sum(a) * 3 - sum(nums)
    return a / 2
