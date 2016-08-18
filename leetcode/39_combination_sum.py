"""
Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where
the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [2, 3, 6, 7] and target 7,
A solution set is:
[
  [7],
  [2, 2, 3]
]
==================================
The caveat here is a number can be used multiple times otherwise this is simply a sorted list problem.
So in addition to moving the left and right pointers, we also need to check if multiple of those numbers can
sum up to target value.
"""


def combinationSum(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    def dfs(candidates, target, start, valueList):
        length = len(candidates)
        if target == 0:
            return res.append(valueList)
        for i in xrange(start, length):
            if target < candidates[i]:
                return
            dfs(candidates, target - candidates[i], i, valueList + [candidates[i]])

    candidates.sort()
    res = []
    dfs(candidates, target, 0, [])
    return res
