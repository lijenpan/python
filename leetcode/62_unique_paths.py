"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Note: m and n will be at most 100.
==================================
I was thinking brute force but apparently there are formulas for this question:
1. Factorial: maxCount = columns! / (rows! (rows - columns)!
2. The dynamic programming way: grid[i][j] = grid[i-1][j] + grid[i][j-1].
"""


def uniquePaths(rows, columns):
    """
    :type rows: int
    :type n: int
    :rtype: int
    """
    grid = [[1 for _ in xrange(0, columns)] for _ in xrange(0, rows)]
    for i in xrange(1, columns):
        for j in xrange(1, rows):
            grid[j][i] = grid[j - 1][i] + grid[j][i - 1]
    return grid[rows - 1][columns - 1]
