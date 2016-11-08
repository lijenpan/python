"""
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear
exactly twice. Find the two elements that appear only once.

For example:

Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].

Note:
The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
===============================
You can use Counter or dict. But for constant space complexity you have to use bit operation as explained here
https://discuss.leetcode.com/topic/21613/c-o-n-time-o-1-space-7-line-solution-with-detail-explanation.
"""

def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    xor = reduce(operator.xor, nums)
    ans = reduce(operator.xor, (x for x in nums if x & xor & -xor))
    return [ans, ans ^ xor]
