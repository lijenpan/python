"""
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.
Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water,
and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes"
(water inside that isn't connected to the water around the island). One cell is a square with side length 1.
The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example:

[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Answer: 16
===============================
The idea is pretty simple. When there is a 1, look for adjacent 1.
Again, Stefan's answer is just brilliant: https://discuss.leetcode.com/topic/68778/short-python/2
"""


def islandPerimeter(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    def water_around(y, x):
        return ((x == 0 or grid[y][x - 1] == 0) +
                (x == len(grid[0]) - 1 or grid[y][x + 1] == 0) +
                (y == 0 or grid[y - 1][x] == 0) +
                (y == len(grid) - 1 or grid[y + 1][x] == 0))

    return sum(water_around(y, x) for y in xrange(len(grid)) for x in xrange(len(grid[0])) if grid[y][x])
