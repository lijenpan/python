"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
==================================
Q46 works here too.
"""


def permuteUnique(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    def nextPermutation(nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                break
        else:
            nums.reverse()
            return
        for j in range(len(nums) - 1, i, -1):
            if nums[j] > nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                break
        for j in range(0, (len(nums) - i) // 2):
            nums[i + j + 1], nums[len(nums) - j - 1] = nums[len(nums) - j - 1], nums[i + j + 1]
    res = [nums]
    while True:
        copy = nums[:]
        nextPermutation(copy)
        if copy in res:
            break
        nums = copy
        res.append(nums)
    return res
