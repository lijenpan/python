"""
Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k),
where h is the height of the person and k is the number of people in front of this person who have a height greater
than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.

Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
===============================
This problem seems complicated at first. But if we think the problem statement in reverse, all the short people are
ignored. In other words, to the tallest people they don't take other people into account. So k essentially is the index
in the list. For example,
Sorted by height --> [[7,0], [7,1], [6,1], [5,0], [5,2], [4,4]]
Loop 1: [[7,0]]
Loop 2: [[7,0], [7,1]]
Loop 3: [[7,0], [6,1], [7,1]]
Loop 4: [[5,0], [7,0], [6,1], [7,1]]
Loop 5: [[5,0], [7,0], [5,2], [6,1], [7,1]]
Loop 6: [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

Which is what we want.
"""


def reconstructQueue(people):
    """
    :type people: List[List[int]]
    :rtype: List[List[int]]
    """
    people.sort(key=lambda (h, k): (-h, k))
    queue = []
    for p in people:
        queue.insert(p[1], p)
    return queue
