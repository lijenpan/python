"""
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.
1. Each row must have the numbers 1-9 occurring just once.
2. Each column must have the numbers 1-9 occurring just once.
3. And the numbers 1-9 must occur just once in each of the 9 sub-boxes of the grid.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
======================
I guess the caveat is how we compute the indices for Rule 3.
"""


def isValidSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    for i in xrange(0, 9):
        if board[i].count('.') + len(set(board[i])) - 1 != 9:
            return False
    for i in xrange(0, 9):
        col = [board[j][i] for j in xrange(9)]
        if col.count('.') + len(set(col)) - 1 != 9:
            return False
    for i in (0, 3, 6):
        for j in (0, 3, 6):
            square = [board[i + m][j + n] for m in (0, 1, 2) for n in (0, 1, 2)]
            if square.count('.') + len(set(square)) - 1 != 9:
                return False
    return True
