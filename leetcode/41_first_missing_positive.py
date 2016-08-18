"""
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
==================================
Can't use common sorting algorithm. Can't allocate new list to sort numbers in sorted order. This is indeed hard.
I can't think of a solution that can do this is one pass. And other people's solutions are swapping/re-ordering
the list until adjacent numbers are +/- 1 of each other and then run one more pass to find the answer. That's O(3n)!

Turns out that O(3n) is O(n). So we can actually use count sort.
"""


def firstMissingPositive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 0:
        return 1
    i = 0
    while i < len(nums):
        if 0 < nums[i] <= len(nums) and nums[nums[i] - 1] != nums[i]:
            tmp = nums[nums[i] - 1]
            nums[nums[i] - 1] = nums[i]
            nums[i] = tmp
            i -= 1
        i += 1
    for i in xrange(0, len(nums)):
        if nums[i] != i + 1:
            return i + 1
    return len(nums) + 1
