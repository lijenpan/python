"""
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
==============================
The base case is keeping track visited nodes, which is space O(n).
The bonus point introduces "different speed". Having two pointers travel the list in different speed.
Namely p1 = head.next.next and p2 = head.next. The idea is if there is a cycle p1 will eventually catch
up to p2.
"""


def hasCycle(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    return False
