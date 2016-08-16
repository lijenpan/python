"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
==================================
The idea is put all pointers in a list, pop the one with smallest value, move that pointer, repeat.
In Python heaps are binary trees implemented using arrays for which heap[k] < heap[2*k + 1] and heap[k] <= heap[2*k+2].
The interesting property of a heap is that its smallest element is always the root.
"""
import heapq


def mergeKLists(lists):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """
    heap = []
    for node in lists:
        if node:
            heap.append((node.val, node))
    heapq.heapify(heap)
    head = ListNode(0)
    curr = head
    while heap:
        pop = heapq.heappop(heap)
        curr.next = ListNode(pop[0])
        curr = curr.next
        if pop[1].next:
            heapq.heappush(heap, (pop[1].next.val, pop[1].next))
    return head.next
