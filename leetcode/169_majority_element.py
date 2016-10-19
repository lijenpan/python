"""
Given an array of size n, find the majority element. The majority element is the element that appears more than
n/2 times.

You may assume that the array is non-empty and the majority element always exist in the array.
==============================
Naive implementation will get you Time Limit Exceeded.
Using Counter is still not fast enough.
Since these are numbers and majority element appears more than n/2 times. We can optimize by sorting the array
and the element we want is in the middle.
"""


def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    return sorted(nums)[len(nums) / 2]
