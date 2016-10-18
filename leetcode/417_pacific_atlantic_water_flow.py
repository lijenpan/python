"""
Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the
"Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Note:
The order of returned grid coordinates does not matter.
Both m and n are less than 150.
Example:

Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).
==============================
Improving from brutal force approach, DFS is probably the way to go. Counting from outside edge of Pacific and Atlantic
in. And then cross match.

Java version: https://discuss.leetcode.com/topic/62401/java-dfs-17ms
"""


def pacificAtlantic(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[List[int]]
    """
    m = len(matrix)
    n = len(matrix[0]) if m else 0
    if m * n == 0:
        return []
    topEdge = [(0, y) for y in range(n)]
    leftEdge = [(x, 0) for x in range(m)]
    pacific = set(topEdge + leftEdge)
    bottomEdge = [(m - 1, y) for y in range(n)]
    rightEdge = [(x, n - 1) for x in range(m)]
    atlantic = set(bottomEdge + rightEdge)

    def bfs(vset):
        dz = zip((1, 0, -1, 0), (0, 1, 0, -1))
        queue = list(vset)
        while queue:
            hx, hy = queue.pop(0)
            for dx, dy in dz:
                nx, ny = hx + dx, hy + dy
                if 0 <= nx < m and 0 <= ny < n:
                    if matrix[nx][ny] >= matrix[hx][hy]:
                        if (nx, ny) not in vset:
                            queue.append((nx, ny))
                            vset.add((nx, ny))

    bfs(pacific)
    bfs(atlantic)
    result = pacific & atlantic
    return map(list, result)
