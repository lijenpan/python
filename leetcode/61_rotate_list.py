"""
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
==================================
Since there is no in-place constraint, this is easy.
"""


def rotateRight(head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """
    if k == 0:
        return head
    if head is None:
        return head
    dummy = ListNode(0)
    dummy.next = head
    p = dummy
    count = 0
    while p.next:
        p = p.next
        count += 1
    p.next = dummy.next
    step = count - (k % count)
    for i in xrange(0, step):
        p = p.next
    head = p.next
    p.next = None
    return head
