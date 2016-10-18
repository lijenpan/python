"""
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
==============================
Just be careful about the None case in recursion.
"""


def sumOfLeftLeaves(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    sum = 0
    if not root:
        return 0
    if root.left and root.left.left is None and root.left.right is None:
        sum += root.left.val
    sum += sumOfLeftLeaves(root.left) + sumOfLeftLeaves(root.right)
    return sum
