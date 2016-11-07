"""
Given a non-empty integer array of size n, find the minimum number of moves required to make all array elements equal,
where a move is incrementing n - 1 elements by 1.

Example:

Input:
[1,2,3]

Output:
3

Explanation:
Only three moves are needed (remember each move increments two elements):

[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
==============================
I wouldn't classify this as easy because brute force will get you TLE. Unless you can think in reverse, meaning
increase all but one element by 1 is the same as decrease one element by 1 so all reached the minimum, you won't
be able to solve this without hitting TLE.
"""


def minMoves(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    return sum(nums) - len(nums) * min(nums)
