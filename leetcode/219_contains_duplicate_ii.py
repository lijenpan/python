"""
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the
array such that nums[i] = nums[j] and the difference between i and j is at most k.
==============================
It's the same sliding window trick but don't slice the array.
"""


def containsNearbyDuplicate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    h = {}
    for i, num in enumerate(nums):
        if num in h and i - h[num] <= k:
            return True
        h[num] = i
    return False
