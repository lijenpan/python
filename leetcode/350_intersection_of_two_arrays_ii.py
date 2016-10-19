"""
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.

Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements
into the memory at once?
==============================

"""
from collections import Counter

def intersect(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    all_numbers = set(nums1) | set(nums2)
    n1_counter = Counter(nums1)
    n2_counter = Counter(nums2)
    res = []
    for n in all_numbers:
        if n1_counter[n] and n2_counter[n]:
            res.extend([n] * min(n1_counter[n], n2_counter[n]))
    return res
