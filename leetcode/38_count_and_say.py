"""
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.
======================
I was quite confused in the beginning thinking how can this be easy?! We are converting numbers to words.

After reading the problem statement couple more times, I think it means:
n = 1 return 1
n = 2 because n = 1 is 1 so there is one 1 return 11
n = 3 because n = 2 is 11 so there are two 1s return 21
n = 4 because n = 3 is 21 so there are one 2 and one 1 return 1211

Very badly worded problem...
"""


def count(s):
    t = ''
    count = 0
    curr = '#'
    for i in s:
        if i != curr:
            if curr != '#':
                t += str(count) + curr
            curr = i
            count = 1
        else:
            count += 1
    t += str(count) + curr
    return t


def countAndSay(n):
    """
    :type n: int
    :rtype: str
    """
    s = '1'
    for i in range(2, n + 1):
        s = self.count(s)
    return s
