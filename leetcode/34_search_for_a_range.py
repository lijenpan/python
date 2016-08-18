"""
Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
==================================
Can't use List.index().
"""


def searchRange(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    start = end = max(len(nums) / 2 - 1, 0)
    res = [-1, -1]
    while True:
        if nums[start] < target:
            break
        if nums[start] == target:
            res[0] = start
            if res[1] == -1:
                res[1] = start
        start -= 1
        if start < 0:
            break

    while True:
        if nums[end] > target:
            break
        if nums[end] == target:
            res[1] = end
            if res[0] == -1:
                res[0] = end
        end += 1
        if end > len(nums) - 1:
            break
    return res
