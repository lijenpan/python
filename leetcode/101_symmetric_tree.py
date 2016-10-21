"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.
==============================
Recursive makes more sense to me.
"""


def isSymmetric(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    if not root:
        return True

    return self.helper(root.left, root.right)


def helper(left, right):
    if left and right:
        if left.val == right.val:
            return helper(left.left, right.right) and helper(left.right, right.left)
        else:
            return False
    else:
        return left == right
