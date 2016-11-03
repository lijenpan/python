"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
==============================
Stefan as always have shortest code: https://discuss.leetcode.com/topic/16869/3-lines-in-every-language. But I
value perform over less code.
"""


def minDepth(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    d = 0
    if root is None:
        return d
    sq = [root]
    while sq:
        temp = []
        d += 1
        for i in sq:
            if i.left or i.right:
                if i.left is not None:
                    temp.append(i.left)
                if i.right is not None:
                    temp.append(i.right)
            else:
                return d
        sq = temp
