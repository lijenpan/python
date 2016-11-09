"""
Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],
   1
    \
     2
    /
   3
return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?
===============================

"""


def inorderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    if not root:
        return []

    stack = [root]
    ans = []

    while stack:
        node = stack.pop()
        if isinstance(node, int):
            ans.append(node)
            continue
        if node.right:  # if has right node, push into stack
            stack.append(node.right)
        stack.append(node.val)  # Push VALUE into stack, in between left and right
        if node.left:  # if has left node, push into stack
            stack.append(node.left)

    return ans
