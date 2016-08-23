"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
==================================
Dynamic programming?
"""


def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    dp = [1 for _ in xrange(0, n + 1)]
    for i in xrange(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
