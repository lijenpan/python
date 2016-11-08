"""
Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product
of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity?
(Note: The output array does not count as extra space for the purpose of space complexity analysis.)
===============================
Brilliant solution: https://discuss.leetcode.com/topic/18983/python-solution-accepted-o-n-time-o-1-space
"""


def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    p = 1
    n = len(nums)
    output = []
    for i in xrange(0, n):
        output.append(p)
        p *= nums[i]
    p = 1
    for i in xrange(n - 1, -1, -1):
        output[i] *= p
        p *= nums[i]
    return output
