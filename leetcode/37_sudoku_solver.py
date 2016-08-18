"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'.

You may assume that there will be only one unique solution.
==================================
I would start filling in row or column with the at least empty slots and then work my way forward.
But not sure how I can code an algorithm to do that. Brute force it is.
"""


class Solution:
    def solveSudoku(self, board):
        def isValid(x, y):
            tmp = board[x][y]; board[x][y] = 'D'
            for i in xrange(0, 9):
                if board[i][y] == tmp:
                    return False
            for i in xrange(0, 9):
                if board[x][i] == tmp:
                    return False
            for i in xrange(0, 3):
                for j in xrange(0, 3):
                    if board[(x/3)*3+i][(y/3)*3+j] == tmp:
                        return False
            board[x][y] = tmp
            return True

        def brute_force(board):
            for i in xrange(0, 9):
                for j in xrange(0, 9):
                    if board[i][j] == '.':
                        for k in '123456789':
                            board[i][j] = k
                            if isValid(i, j) and brute_force(board):
                                return True
                            board[i][j] = '.'
                        return False
            return True
        brute_force(board)
