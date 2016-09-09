"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
==================================
Just move the pointer to next node when encounter duplicates. Easy.
"""


def deleteDuplicates(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if head is None or head.next is None:
        return head
    p = head
    while p.next:
        if p.val == p.next.val:
            p.next = p.next.next
        else:
            p = p.next
    return head
