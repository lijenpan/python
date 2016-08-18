"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where
it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0
==================================
Why is this medium?
"""


def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    for i in xrange(0, len(nums)):
        if nums[i] >= target:
            return i
    return i + 1
