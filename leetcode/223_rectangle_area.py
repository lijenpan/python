"""
https://leetcode.com/problems/rectangle-area/
==============================

"""


def computeArea(self, A, B, C, D, E, F, G, H):
    """
    :type A: int
    :type B: int
    :type C: int
    :type D: int
    :type E: int
    :type F: int
    :type G: int
    :type H: int
    :rtype: int
    """
    def overlap(v):
        sum_len = abs(v[0] - v[1]) + abs(v[2] - v[3])
        v.sort()
        max_len = abs(v[0] - v[-1])
        return sum_len - max_len if sum_len >= max_len else 0

    return abs(C - A) * abs(D - B) + abs(G - E) * abs(H - F) - overlap([A, C, E, G]) * overlap([B, D, F, H])
