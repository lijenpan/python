"""
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?
==============================

"""


def getRow(rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    if rowIndex == 0:
        return [1]
    res = []
    for i in xrange(rowIndex+1):
        new_value = 1
        row = [new_value]
        for j in xrange(i):
            new_value = new_value * (i - j) * 1 / (j + 1)
            row.append(new_value)
        res.append(row)
    return res[rowIndex]
