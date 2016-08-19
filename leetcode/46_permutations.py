"""
Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
==================================
We can re-use Q31 code.
"""


def permute(nums):
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
