"""
Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
==============================
This is a classic linked list problem. We need to find the length of each lists and move the pointer to longer list
forward. Stupid MLE!
"""
import gc


def getIntersectionNode(headA, headB):
    """
    :type headA, headB: ListNode
    :rtype: ListNode
    """
    a = headA
    b = headB
    a_count = b_count = 0
    while a is not None:
        a = a.next
        a_count += 1
    while b is not None:
        b = b.next
        b_count += 1

    while a_count > 0 and b_count > 0:
        if a_count > b_count:
            headA = headA.next
            a_count -= 1
        if b_count > a_count:
            headB = headB.next
            b_count -= 1
        if a_count == b_count:
            if headA == headB:
                gc.collect()
                return headA
            else:
                headA = headA.next
                headB = headB.next
                a_count -= 1
                b_count -= 1
    return None
