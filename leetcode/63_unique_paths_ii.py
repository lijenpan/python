"""
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.

Note: m and n will be at most 100.
==================================
Building on Q62, we represent path cannot travel or travelled as 0.
So basically we flip the board and apply the same code.

Can't cheat by using formula here.
"""


def uniquePathsWithObstacles(obstacleGrid):
    """
    :type obstacleGrid: List[List[int]]
    :rtype: int
    """
    rows = len(obstacleGrid)
    columns = len(obstacleGrid[0])

    dp = [[0 for _ in xrange(columns)] for _ in xrange(rows)]
    for i in xrange(columns):
        if obstacleGrid[0][i] == 0:
            dp[0][i] = 1
        else:
            break
    for i in xrange(rows):
        if obstacleGrid[i][0] == 0:
            dp[i][0] = 1
        else:
            break

    for i in xrange(1, rows):
        for j in xrange(1, columns):
            dp[i][j] = 0 if obstacleGrid[i][j] == 1 else dp[i - 1][j] + dp[i][j - 1]
    return dp[rows - 1][columns - 1]
