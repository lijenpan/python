"""
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:
Given n will always be valid.
Try to do this in one pass.
==================================
First thing came to mind is find the value of nth node and then remove by index. But the problem statement says try
to do this in one pass. So we need to create a second pointer that start from the head, let the first pointer moves
ahead by n steps, and then move both pointers at the same time. When the first pointer reaches the end, second pointer
is what we want to remove.
"""


def removeNthFromEnd(head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    dummy = ListNode(0)
    dummy.next = head
    tmp = dummy
    for i in xrange(0, n):
        head = head.next
    while head is not None:
        head = head.next
        tmp = tmp.next
    tmp.next = tmp.next.next
    return dummy.next

