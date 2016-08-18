"""
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.

For example,
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
==================================
This is not trivial way of thinking in terms of traversing from left and right. I consider this very hard.

General approach is given height[i] can hold water, there must be two greater number to the left (height[L])
and to the right (height[R]). And the maximum is min(height[L], height[R]) - height[i].

So, let L = 0 and R = len(height) - 1 and current_height = 0, if height[L] < height[R],
we compare current_height against height[L], the difference is what we can hold. L += 1

Similarly height[L] > height[R], R -= 1. Then writing the code is actually pretty simple.
"""


def trap(height):
    """
    :type height: List[int]
    :rtype: int
    """
    L = 0
    R = len(height) - 1
    current_height = 0
    total = 0
    while L < R:
        if height[L] < height[R]:
            current_height = max(height[L], current_height)
            total += current_height - height[L]
            L += 1
        else:
            current_height = max(height[R], current_height)
            total += current_height - height[R]
            R -= 1
    return total
