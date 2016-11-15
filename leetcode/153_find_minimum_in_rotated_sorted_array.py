"""
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.
===============================
The answer can be as simple as min(nums). But of course there is optimization can be done here. Divide and conquer.
"""


def findMin(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    start = 0
    end = len(nums) - 1
    while start <= end:
        mid = (start + end) / 2
        if nums[mid] < nums[end]:
            end = mid
        else:
            start = mid + 1
    return nums[end]
