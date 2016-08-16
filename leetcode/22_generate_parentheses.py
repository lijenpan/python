"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
==================================
I confess I was lost on this one. So I asked a coworker and he said depth first search solves this problem. Oh yeah...
"""


def dfs(l, r, item, res):
    if r < l:
        # If left and right are unbalanced, not a valid combination
        return
    if l == 0 and r == 0:
        res.append(item)
    if l > 0:
        dfs(l - 1, r, item + '(', res)
    if r > 0:
        dfs(l, r - 1, item + ')', res)


def generateParenthesis(n):
    """
    :type n: int
    :rtype: List[str]
    """
    if n == 0:
        return []
    res = []
    dfs(n, n, '', res)
    return res
