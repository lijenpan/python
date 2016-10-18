"""
Invert a binary tree.

     4
   /   \
  2     7
 / \   / \
1   3 6   9
to
     4
   /   \
  7     2
 / \   / \
9   6 3   1
==============================
Use recursion. Don't be the next Max Howell.
"""


def invertTree(root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    if root is not None:
        root.left, root.right = invertTree(root.right), invertTree(root.left)
    return root
