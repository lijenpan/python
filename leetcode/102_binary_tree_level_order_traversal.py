"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
==============================

"""


def levelOrder(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    def _level(root, level, values):
        if root is None:
            return
        values[level] = values.get(level, []) + [root.val]
        _level(root.left, level + 1, values)
        _level(root.right, level + 1, values)

    res = {}
    _level(root, 0, res)
    return res.values()
