"""
Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

Supposed the linked list is 1 -> 2 -> 3 -> 4 and you are given the third node with value 3, the linked list
should become 1 -> 2 -> 4 after calling your function.
==============================
I was confused about what the question was asking without giving the root. Then I realize the question
was simply asking to point the given node to the next one. Thus delete the given node. Simple.
"""


def deleteNode(node):
    """
    :type node: ListNode
    :rtype: void Do not return anything, modify node in-place instead.
    """
    node.val = node.next.val
    node.next = node.next.next
