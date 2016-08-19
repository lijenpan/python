"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to
the last index.)

Note:
You can assume that you can always reach the last index.
==================================
The idea is to use start and end to record start point and max jump. Every time we jump update start to end + 1.

Then I saw someone came up with this solution in the discussion:
"last" keeps track of maximum distance that has been reached by using the minimum steps ("ret") whereas
"curr" is the maximum distance that can be reached by using ret + 1 steps. Thus,
curr = max(i + nums[i]) where 0 <= i <= last.

Genius! To put that in code:

def jump(nums):
    ret = last = curr = 0
    for i in xrange(0, len(nums):
        if i > last:
            last = curr
            ret += 1
        curr = max(curr, i + nums[i])
    return ret
"""


def jump(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n, start, end, step = len(nums), 0, 0, 0
    while end < n - 1:
        step += 1
        maxend = end + 1
        for i in range(start, end + 1):
            if i + nums[i] >= n - 1:
                return step
            maxend = max(maxend, i + nums[i])
        start, end = end + 1, maxend
    return step
