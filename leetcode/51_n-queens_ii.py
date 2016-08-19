"""
Follow up for N-Queens problem.

Now, instead outputting board configurations, return the total number of distinct solutions.
==================================
This is a no-brainer coming from Q51.
"""


class Solution:
    def totalNQueens(self, n):
        self.res = []
        self.solve(n, 0, [-1 for _ in xrange(n)])
        return len(self.res)

    def solve(self, n, currQueenNum, board):
        if currQueenNum == n:
            oneAnswer = [['.' for _ in xrange(n)] for _ in xrange(n)]
            for i in xrange(n):
                oneAnswer[i][board[i]] = 'Q'
                oneAnswer[i] = ''.join(oneAnswer[i])
            self.res.append(oneAnswer)
            return
        # try to put a Queen in (currQueenNum, 0), (currQueenNum, 1), ..., (currQueenNum, n-1)
        for i in xrange(n):
            valid = True  # test whether board[currQueenNum] can be i or not
            for k in xrange(currQueenNum):
                # check column
                if board[k] == i:
                    valid = False
                    break
                # check diagonal
                if abs(board[k] - i) == currQueenNum - k:
                    valid = False
                    break
            if valid:
                board[currQueenNum] = i
                self.solve(n, currQueenNum + 1, board)
