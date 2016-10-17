"""
Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the
maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
==============================
Cannot use max()... And the caveat is you have to use minus infinity not -2^31.
"""


def thirdMax(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    count = 0
    top = [float("-inf")] * 3
    for num in nums:
        if num > top[0]:
            top[0], top[1], top[2] = num, top[0], top[1]
            count += 1
        elif num != top[0] and num > top[1]:
            top[1], top[2] = num, top[1]
            count += 1
        elif num != top[0] and num != top[1] and num >= top[2]:
            top[2] = num
            count += 1

    if count < 3:
        return top[0]

    return top[2]
