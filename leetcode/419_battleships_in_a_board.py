"""
Given an 2D board, count how many different battleships are in it. The battleships are represented with 'X's, empty slots are represented with '.'s. You may assume the following rules:

You receive a valid board, made of only battleships or empty slots.
Battleships can only be placed horizontally or vertically. In other words, they can only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column), where N can be of any size.
At least one horizontal or vertical cell separates between two battleships - there are no adjacent battleships.

Example:
X..X
...X
...X
In the above board there are 2 battleships.

Invalid Example:
...X
XXXX
...X
This is not a valid board - as battleships will always have a cell separating between them.

Your algorithm should not modify the value of the board.
==============================
I can't think of anything but just implement the rules.
"""


def countBattleships(board):
    """
    :type board: List[List[str]]
    :rtype: int
    """
    res = 0
    for row in xrange(0, len(board)):
        for col in xrange(0, len(board[0])):
            if all([board[row][col] == 'X',
                    not col or board[row][col - 1] != 'X',  # vertical space, or can be more explicitly written as x == 0 or ...
                    not row or board[row - 1][col] != 'X'  # horizontal space
                   ]):
                res += 1
    return res
