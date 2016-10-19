"""
Given an array of integers, find if the array contains any duplicates. Your function should return true if any value
appears at least twice in the array, and it should return false if every element is distinct.
==============================
If length of set of nums does not match length of nums, we have duplicates.
"""


def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    return not len(set(nums)) == len(nums) if nums else False
