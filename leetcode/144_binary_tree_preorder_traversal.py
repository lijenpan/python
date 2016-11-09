"""
iven a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,2,3].

Note: Recursive solution is trivial, could you do it iteratively?
===============================
Preorder is root, left, and then right.
"""


def preorderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    return [root.val] + preorderTraversal(root.left) + preorderTraversal(root.right) if root is not None else []
