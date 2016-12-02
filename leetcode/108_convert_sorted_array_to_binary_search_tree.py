"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
===============================
We can just follow the BST insert logic. But since the input is already sorted, the mid point will be the root.
"""


def sortedArrayToBST(nums):
    """
    :type nums: List[int]
    :rtype: TreeNode
    """
    if not nums:
        return None
    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    root.left = sortedArrayToBST(nums[:mid])
    root.right = sortedArrayToBST(nums[mid+1:])
    return root
