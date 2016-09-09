"""
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers
from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
==================================
A little twist. Need two pointers.
"""


def deleteDuplicates(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if head is None or head.next is None:
        return head

    new_head = ListNode(-1)
    new_head.next = head
    parent = new_head
    cur = head
    while cur is not None and cur.next is not None:
        if cur.val == cur.next.val:
            val = cur.val
            while cur is not None and val == cur.val:
                cur = cur.next
            parent.next = cur
        else:
            cur = cur.next
            parent = parent.next

    return new_head.next
