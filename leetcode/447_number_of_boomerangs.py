"""
Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that
the distance between i and j equals the distance between i and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in
the range [-10000, 10000] (inclusive).

Example:
Input:
[[0,0],[1,0],[2,0]]

Output:
2

Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
==============================
Brute force will most likely get you TLE because the operation will be O(n^2). But I can't think of a way to not
performing O(n^2), I just speed it up by bucketing with dict.
"""


def numberOfBoomerangs(points):
    """
    :type points: List[List[int]]
    :rtype: int
    """
    res = 0
    for i in xrange(len(points)):
        pd = {}
        for j in xrange(len(points)):
            if j != i:
                d = pow(abs(points[i][0] - points[j][0]), 2) + pow(abs(points[i][1] - points[j][1]), 2)
                key = str(d)
                if key in pd:
                    pd[key] += 1
                else:
                    pd[key] = 1
        for p in pd:
            if pd[p] > 1:
                # Combination of coordinates in this bucket satisfies boomerang.
                res += pd[p] * (pd[p] - 1)
    return res
