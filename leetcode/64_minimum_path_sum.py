"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which
minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
==================================
A variation of Q63. Same DP approach still applies. But we keep track the minimum sum.
"""


def minPathSum(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    rows = len(grid)
    columns = len(grid[0])
    dp = [[0 for _ in xrange(columns)] for _ in xrange(rows)]
    dp[0][0] = grid[0][0]

    for i in xrange(1, columns):
        dp[0][i] = dp[0][i - 1] + grid[0][i]
    for i in xrange(1, rows):
        dp[i][0] = dp[i - 1][0] + grid[i][0]

    for i in xrange(1, rows):
        for j in xrange(1, columns):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
    return dp[rows - 1][columns - 1]
