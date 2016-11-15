"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 <= k <= BST's total elements.

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently?
How would you optimize the kthSmallest routine?

Hint:

Try to utilize the property of a BST.
What if you could modify the BST node's structure?
The optimal runtime complexity is O(height of BST).
===============================
Brilliant use of yield: https://discuss.leetcode.com/topic/18279/pythonic-approach-with-generator/2
"""


def kthSmallest(root, k):
    """
    :type root: TreeNode
    :type k: int
    :rtype: int
    """
    def inorder(root):
        if root is not None:
            for val in inorder(root.left):
                yield val
            yield root.val
            for val in inorder(root.right):
                yield val

    for val in inorder(root):
        if k == 1:
            return val
        else:
            k -= 1
