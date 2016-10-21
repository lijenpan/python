"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees
of every node never differ by more than 1.
==============================

"""


def isBalanced(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    def depth(node):
        if not node:
            return 0
        left = depth(node.left)
        right = depth(node.right)
        if abs(left - right) > 1:
            # return False check continue the loop and return incorrect result
            raise Exception
        return max(left, right) + 1

    if not root:
        return True
    try:
        return abs(depth(root.left) - depth(root.right)) <= 1
    except:
        return False
