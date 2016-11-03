"""
Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5
==============================
Need a dummy to head.
"""


def removeElements(head, val):
    """
    :type head: ListNode
    :type val: int
    :rtype: ListNode
    """
    dummy = ListNode(0)
    dummy.next = head
    p = dummy
    while p.next:
        if p.next.val == val:
            p.next = p.next.next
        else:
            p = p.next
    return dummy.next
