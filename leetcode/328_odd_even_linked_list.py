"""
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking
about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example:
Given 1->2->3->4->5->NULL,
return 1->3->5->2->4->NULL.

Note:
The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on...
===============================
The idea is simple. Two points - one traverse odd nodes and the other even nodes. When odd nodes reaches the end
point next to the start of even nodes. But not so easy to get it right 100%.
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return self.val

def oddEvenList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if head is None or head.next is None or head.next.next is None:
        return head
    odd_node = head
    even_stater = head.next
    while odd_node.next is not None and odd_node.next.next is not None:
        even_node = odd_node.next
        odd_node.next = even_node.next
        odd_node = odd_node.next
        even_node.next = odd_node.next
    odd_node.next = even_stater
    return head
