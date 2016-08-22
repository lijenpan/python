"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
==================================
It's similar to Q45. But instead of finding the minimum steps to reach the end we just need to know if we can.
"""


def canJump(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    step = nums[0]
    for i in xrange(1, len(nums)):
        if step > 0:
            step -= 1
            step = max(step, nums[i])
        else:
            return False
    return True
