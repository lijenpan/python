"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
=====================================
Yes, this is hard to get it right. Maybe we can break the process down by reverse one subset of the list at a time.
"""


def reverse(start, end):
    # This is just a regular reverse LinkedList function
    dummy = ListNode(0)
    dummy.next = start
    while dummy.next != end:
        tmp = start.next
        start.next = tmp.next
        tmp.next = dummy.next
        dummy.next = tmp
    return end, start


def reverseKGroup(head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """
    dummy = ListNode(0)
    dummy.next = head
    start = dummy
    while start.next:
        end = start
        for i in xrange(0, k - 1):
            end = end.next
            if end.next is None:
                return dummy.next
        new_start, new_end = reverse(start.next, end.next)
        start.next = new_start
        start = new_end
    return dummy.next
