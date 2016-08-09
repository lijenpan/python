"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution.
"""


def two_sum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    d = {}
    for i in xrange(len(nums)):
        x = nums[i]
        if target - x in d:
            return [d[target - x], i]
        d[x] = i

if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    assert two_sum(nums, target) == [0, 1]
