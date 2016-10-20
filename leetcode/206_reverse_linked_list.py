"""
Reverse a singly linked list.
==============================

"""


def reverseList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    temp = None
    while head:
        head.next, temp, head = temp, head, head.next
    return temp
