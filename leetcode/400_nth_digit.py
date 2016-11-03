"""
Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Note:
n is positive and will fit within the range of a 32-bit signed integer (n < 231).

Example 1:

Input:
3

Output:
3
Example 2:

Input:
11

Output:
0

Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.
==============================
Brute force will get you TLE. So we need to get clever about how to check the sequence.
Similar to this guys's idea: https://discuss.leetcode.com/topic/60286/4-liner-in-python-and-complexity-analysis
But easier to read I think?
"""


def findNthDigit(n):
    """
    :type n: int
    :rtype: int
    """
    n -= 1  # adjust to 0 base index
    for digits in xrange(1, 11):
        first = 10**(digits - 1)
        if n < 9 * first * digits:
            return int(str(first + n / digits)[n % digits])
        n -= 9 * first * digits
