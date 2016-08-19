"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate
a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
==================================
Keeps coming back to DFS. But brute force makes more sense to me. Just iterate through all possibilities
and see which ones checks out.
"""


class Solution:
    def solveNQueens(self, n):
        self.res = []
        self.solve(n, 0, [-1 for _ in xrange(n)])
        return self.res

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
