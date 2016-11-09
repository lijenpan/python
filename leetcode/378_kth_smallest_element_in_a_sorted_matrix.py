"""
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element
in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
Note:
You may assume k is always valid, 1 <= k <= n^2.
===============================
Yeah okay. Try to come up with this during the interview:
https://discuss.leetcode.com/topic/53126/o-n-from-paper-yes-o-rows
"""


def kthSmallest(matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    flat_matrix = [item for sublist in matrix for item in sublist]
    flat_matrix.sort()
    if len(flat_matrix) < k:
        return flat_matrix[-1]
    else:
        return flat_matrix[k - 1]
