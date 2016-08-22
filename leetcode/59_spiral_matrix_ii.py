"""
Given an integer n, generate a square matrix filled with elements from 1 to n^2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
==================================
Let's solve this like a normal person.
"""


def generateMatrix(n):
    """
    :type n: int
    :rtype: List[List[int]]
    """
    if n == 0:
        return []
    matrix = [[0 for _ in xrange(0, n)] for _ in xrange(0, n)]
    up = 0
    down = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1
    direct = 0
    count = 0
    while True:
        if direct == 0:
            for i in xrange(left, right + 1):
                count += 1
                matrix[up][i] = count
            up += 1
        if direct == 1:
            for i in xrange(up, down + 1):
                count += 1
                matrix[i][right] = count
            right -= 1
        if direct == 2:
            for i in xrange(right, left - 1, -1):
                count += 1
                matrix[down][i] = count
            down -= 1
        if direct == 3:
            for i in xrange(down, up - 1, -1):
                count += 1
                matrix[i][left] = count
            left += 1
        if count == n * n:
            return matrix
        direct = (direct + 1) % 4
