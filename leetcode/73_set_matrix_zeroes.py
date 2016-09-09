"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

Follow up:
Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
==================================
The question is not very clear because if we process the matrix from top to bottom. Most likely we would
end up with a matrix with all zeroes. However, with this input
[
    [0,0,0,5],
    [4,3,1,4],
    [0,1,1,4],
    [1,2,1,3],
    [0,0,1,1]
]
the expected output is
[
    [0,0,0,0],
    [0,0,0,4],
    [0,0,0,0],
    [0,0,0,3],
    [0,0,0,0]
].
So we need to mark where 0s are and then set them to 0s.
"""


def setZeroes(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """
    rows = len(matrix)
    columns = len(matrix[0])
    row = [False for _ in range(rows)]
    col = [False for _ in range(columns)]
    for i in xrange(0, rows):
        for j in xrange(0, columns):
            if matrix[i][j] == 0:
                row[i] = True
                col[j] = True
    for i in xrange(rows):
        for j in xrange(columns):
            if row[i] or col[j]:
                matrix[i][j] = 0
