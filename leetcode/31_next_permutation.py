"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
==================================
I don't quite understand what this lexicographically permutation means here because to iterate through strings
or integers 1,2,3 should remain the same. But it's not. After some research this question is asking you to implement
C++ STL's next_permutation. Here is how it works:
1. Find last (a) and second to last digit (b) such that a < b.
2. From the end find a digit (c) that is greater than a.
3. Swap a and c and then reverse anything after b.

Yeah what the fuck!
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

