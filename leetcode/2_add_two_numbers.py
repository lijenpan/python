"""
You are given two linked lists representing two non-negative numbers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def add_two_numbers(l1, l2):
    head = ListNode(0)
    pointer = head
    carry = 0
    while True:
        if l1 is not None:
            carry += l1.val
            l1 = l1.next
        if l2 is not None:
            carry += l2.val
            l2 = l2.next
        pointer.val = carry % 10
        carry /= 10
        if l1 is not None or l2 is not None or carry != 0:
            pointer.next = ListNode(0)
            pointer = pointer.next
        else:
            break
    return head

if __name__ == "__main__":
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    head = add_two_numbers(l1, l2)

    while True:
        print head.val
        head = head.next
        if head is None:
            break
