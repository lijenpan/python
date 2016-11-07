"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version
of your product fails the quality check. Since each version is developed based on the previous version, all the
versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the
following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad.
Implement a function to find the first bad version. You should minimize the number of calls to the API.
===============================
You should go straight to binary search. It's also interesting to see inner function is faster than while loop.
"""


def firstBadVersion(n):
    """
    :type n: int
    :rtype: int
    """
    def binary_search(start, end):
        mid = (start + end) / 2
        if isBadVersion(mid):
            if not isBadVersion(mid - 1) or mid == 1:
                return mid
            elif isBadVersion(mid - 1):
                return binary_search(start, mid - 1)
        else:
            return binary_search(mid + 1, end)

    return binary_search(0, n)
