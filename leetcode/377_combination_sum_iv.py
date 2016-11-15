"""
Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that
add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.
Follow up:
What if negative numbers are allowed in the given array?
How does it change the problem?
What limitation we need to add to the question to allow negative numbers?
===============================
I can't think of a better way than DP.
"""


def combinationSum4(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    nums = sorted(nums)
    combs = [1] + [0] * target
    for i in xrange(target + 1):
        for num in nums:
            if num > i:
                break
            if num == i:
                combs[i] += 1
            if num < i:
                combs[i] += combs[i - num]
    return combs[target]


if __name__ == "__main__":
    assert combinationSum4([1, 2, 3], 4) == 7
