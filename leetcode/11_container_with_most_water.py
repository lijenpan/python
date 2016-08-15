"""
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines,
which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container.
======================
I had to read the problem statement a few times to understand what it's asking for. To phrase it another way:
given any two height a[i] and a[j] maximize min(a[i], a[j]) * (i - j).
"""


def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    left = 0
    right = len(height) - 1
    ans = 0
    while left != right:
        if height[left] < height[right]:
            area = height[left] * (right - left)
            left += 1
        else:
            area = height[right] * (right - left)
            right -= 1
        ans = max(ans, area)
    return ans
