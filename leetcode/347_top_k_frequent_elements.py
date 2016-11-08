"""
Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note:
You may assume k is always valid, 1 <= k <= number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
===============================

"""
from collections import Counter
import operator

def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    c = Counter(nums)
    sorted_c = sorted(c.items(), key=operator.itemgetter(1))
    res = []
    for i in xrange(len(sorted_c) - 1, len(sorted_c) - k - 1, -1):
        res.append(sorted_c[i][0])
    return res

if __name__ == "__main__":
    assert topKFrequent([1, 1, 1, 2, 2, 3], 2) == [1, 2]
