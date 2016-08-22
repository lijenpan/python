"""
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
==================================
Looks simple but hard to get it right 100%.

Caveats:
1. Intervals can be out of order.

After sorting intervals, we just need to iterate through it once.
"""


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals = sorted(intervals, key=lambda x: x.start)
        res = []
        for i in intervals:
            if len(res) == 0 or res[-1].end < i.start:
                res.append(i)
            else:
                res[-1].end = max(res[-1].end, i.end)
        return res
