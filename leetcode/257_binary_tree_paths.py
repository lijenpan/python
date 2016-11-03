"""
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]
==============================
Traverse all left nodes and then all right nodes. Then combine.
"""


def binaryTreePaths(root):
    if not root:
        return []
    res = [str(root.val) + '->' + path for path in binaryTreePaths(root.left)]
    res.extend([str(root.val) + '->' + path for path in binaryTreePaths(root.right)])
    return res or [str(root.val)]
