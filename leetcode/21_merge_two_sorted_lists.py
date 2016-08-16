"""
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.
==================================
The problem statement tells you what it wants you to do. So do it!
"""


def mergeTwoLists(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    dummy = ListNode(0)
    tmp = dummy
    while l1 is not None and l2 is not None:
        if l1.val < l2.val:
            tmp.next = l1
            l1 = l1.next
        else:
            tmp.next = l2
            l2 = l2.next
        tmp = tmp.next
    if l1 is not None:
        tmp.next = l1
    else:
        tmp.next = l2
    return dummy.next
