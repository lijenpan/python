"""
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the new length.
==================
Swapping it is! Something is whacky about the test cases.
"""


def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) <= 1:
        return len(nums)
    count = 0
    for i in xrange(0, len(nums)):
        if nums[i] != nums[count]:
            nums[i], nums[count + 1] = nums[count + 1], nums[i]
            count += 1
    return count + 1
