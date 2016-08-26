"""
Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2.
(each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character
==================================
In Python because of difflib. But let's solve this one without help.

I had trouble trying to code up a logic for insert operation. So I looked at how others solved this problem.
Apparently this is also a DP problem: https://www.youtube.com/watch?v=We3YDTzNXEk
"""


def minDistance(word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: int
    """
    m = len(word1) + 1
    n = len(word2) + 1
    dp = [[0 for _ in xrange(n)] for _ in xrange(m)]
    for i in xrange(n):
        dp[0][i] = i
    for i in xrange(m):
        dp[i][0] = i
    for i in xrange(1, m):
        for j in xrange(1, n):
            dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1,
                           dp[i - 1][j - 1] + (0 if word1[i - 1] == word2[j - 1] else 1))
    return dp[m - 1][n - 1]
