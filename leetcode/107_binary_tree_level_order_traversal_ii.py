"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values.
(ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
==============================
Need to keep track of levels.
"""


def levelOrderBottom(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    res = []
    travel(root, 1, res)
    return res


def travel(root, level, res):
    if root is None:
        return False
    if len(res) < level:
        res.insert(0, [])
    idx = len(res) - level
    res[idx].append(root.val)
    travel(root.left, level + 1, res)
    travel(root.right, level + 1, res)
