"""
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C
where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
==================================
Same as last one, but no repeating number.
"""


def combinationSum2(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    def dfs(candidates, target, start, valuelist):
        length = len(candidates)
        if target == 0 and valuelist not in res:
            return res.append(valuelist)
        for i in range(start, length):
            if target < candidates[i]:
                return
            dfs(candidates, target - candidates[i], i + 1, valuelist + [candidates[i]])

    candidates.sort()
    res = []
    dfs(candidates, target, 0, [])
    return res
