import random

class Solution(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        indices = [i for i, x in enumerate(self.nums) if x == target]
        return random.choice(indices)
