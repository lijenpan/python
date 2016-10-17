"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
==============================
I can't think of better way than checking adjacent letters.
"""


def exist(board, word):
    def existRecu(board, word, cur, i, j, visited):
        if cur == len(word):
            return True

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or visited[i][j] or board[i][j] != word[cur]:
            return False

        visited[i][j] = True
        result = existRecu(board, word, cur + 1, i + 1, j, visited) or \
                 existRecu(board, word, cur + 1, i - 1, j, visited) or \
                 existRecu(board, word, cur + 1, i, j + 1, visited) or \
                 existRecu(board, word, cur + 1, i, j - 1, visited)
        visited[i][j] = False

        return result

    visited = [[False for j in xrange(len(board[0]))] for i in xrange(len(board))]

    for i in xrange(len(board)):
        for j in xrange(len(board[0])):
            if existRecu(board, word, 0, i, j, visited):
                return True

    return False

