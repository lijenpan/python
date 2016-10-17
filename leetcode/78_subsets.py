"""
Given a set of distinct integers, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
==============================
Recursion makes more sense to me than DFS. The idea is combine previous two elements and combine them.
For example, first we have [[], [1]]. Then 2 comes, [[], [1], [2], [1, 2]]. So sorting the input list is imperative.
"""


def subsets(nums):
    result = [[]]
    for num in sorted(nums):
        result += [item + [num] for item in result]
    return result


if __name__ == "__main__":
    print subsets([1,2,3])
