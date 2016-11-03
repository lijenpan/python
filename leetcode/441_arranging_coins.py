"""
You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:

n = 5

The coins can form the following rows:
*
* *
* *

Because the 3rd row is incomplete, we return 2.
Example 2:

n = 8

The coins can form the following rows:
*
* *
* * *
* *

Because the 4th row is incomplete, we return 3.
==============================
The naive approach would be keep subtracting coins until there is not enough.
But there is of course an algorithm to solve this in constant time and space.
"""


def arrangeCoins(n):
    """
    :type n: int
    :rtype: int
    """
    return int((1+8*n)**0.5 - 1) / 2
