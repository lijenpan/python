"""
Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
==============================

"""


def isSameTree(p, q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """
    if not (p or q):
        return True
    if not (p and q) or p.val != q.val:
        return False
    else:
        return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
