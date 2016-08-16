"""
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list,
only nodes itself can be changed.
==================
Just need to be careful about the references.
"""


def swapPairs(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if head is None or head.next is None:
        return head
    dummy = ListNode(0)
    dummy.next = head
    p = dummy
    while p.next and p.next.next:
        tmp = p.next.next
        p.next.next = tmp.next
        tmp.next = p.next
        p.next = tmp
        p = p.next.next
    return dummy.next
