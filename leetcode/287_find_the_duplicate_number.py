"""
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least
one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Note:
1. You must not modify the array (assume the array is read only).
2. You must use only constant, O(1) extra space.
3. Your runtime complexity should be less than O(n^2).
4. There is only one duplicate number in the array, but it could be repeated more than once.
======================================
Well there seems be some dispute about whether my solution violates Constraint #2. In my mind, O(1) means
the extra space has no correlation to the input size (e.g. 5 variables). So I see this as acceptable answer.

If you disagree, second approach is for you.
"""


def find_duplicates(nums):
    tmp = 0
    for n in nums:
        if 1 << n & tmp != 0:
            return n
        tmp |= 1 << n


def find_duplicate(nums):
    min = 0
    max = len(nums) - 1
    while min <= max:
        mid = min + (max - min) / 2
        count = 0
        for i in xrange(0, len(nums)):
            if nums[i] <= mid:
                count += 1

        if count > mid:
            max = mid - 1
        else:
            min = mid + 1
    return min
