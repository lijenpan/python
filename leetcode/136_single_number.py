"""
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
==============================
So no dictionary to store the count. XOR?
"""


def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    res = 0
    for n in nums:
        res ^= n
    return res
