"""
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target.
Return the sum of the three integers. You may assume that each input would have exactly one solution.

For example, given array S = {-1 2 1 -4}, and target = 1.
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""


def threeSumClosest(nums, target):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    nums.sort()
    ans = None
    for i in xrange(len(nums)):
        l, r = i + 1, len(nums) - 1
        while l < r:
            s = nums[l] + nums[r] + nums[i]
            if ans is None or abs(s - target) < abs(ans - target):
                ans = s
            if s <= target:
                l += 1
            else:
                r -= 1
    return ans
