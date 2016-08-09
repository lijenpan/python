"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5

=====================================
Okay. This one deserves some explanation. First thing comes to mind is merge two sorted arrays and find the median.
But the time complexity is O((m+n) log(m+n)) which is more than the optimal O(log(m+n)).

The idea is similar to divide and conquer in each array since the arrays are already sorted and keep loop through
until finding the median, which is materialized in find Kth element function.
"""


def find_kth(nums1, nums2, k):
    len_nums1 = len(nums1)
    len_nums2 = len(nums2)
    if len_nums1 > len_nums2:
        return find_kth(nums2, nums1, k)
    if len_nums1 == 0:
        return nums2[k - 1]
    if k == 1:
        return min(nums1[0], nums2[0])
    pa = min(k / 2, len_nums1)
    pb = k - pa
    if nums1[pa - 1] <= nums2[pb - 1]:
        return find_kth(nums1[pa:], nums2, pb)
    else:
        return find_kth(nums1, nums2[pb:], pa)


def find_median_sorted_arrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    len_nums1 = len(nums1)
    len_nums2 = len(nums2)
    if (len_nums1 + len_nums2) % 2 == 1:
        return find_kth(nums1, nums2, (len_nums1 + len_nums2) / 2 + 1)
    else:
        return (find_kth(nums1, nums2, (len_nums1 + len_nums2) / 2) +
                find_kth(nums1, nums2, (len_nums1 + len_nums2) / 2 + 1)) * 0.5


if __name__ == "__main__":
    assert find_median_sorted_arrays([1, 3], [2]) == 2.0
    assert find_median_sorted_arrays([1, 2], [3, 4]) == 2.5
