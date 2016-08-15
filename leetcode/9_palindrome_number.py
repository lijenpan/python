"""
Determine whether an integer is a palindrome. Do this without extra space.
======================
Clarification: extra space means you can still have constant space (e.g. variables) but not O(input size).
People are confused about that. Some takes that extra space literally. If that's true, I don't think you can ever
have a solution for "no extra space".
"""


def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0:
        return False
    if x == 0:
        return True
    if x % 10 == 0:
        return False

    rev = 0
    tmp = x
    while rev < x:
        rev = 10 * rev + tmp % 10
        tmp /= 10
    return rev == x
