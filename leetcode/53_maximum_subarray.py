"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.

More practice:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach,
which is more subtle.
==================================
The linear approach is keep track rolling sum with local and global maximum. A dynamic programming problem.

I can't think of how divide and conquer would work here.
"""


def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    local_max = 0
    global_max = -999

    for i in xrange(0, len(nums)):
        if local_max < 0:
            local_max = 0
        local_max += nums[i]
        global_max = max(local_max, global_max)
    return global_max
