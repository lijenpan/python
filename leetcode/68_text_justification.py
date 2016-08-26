"""
Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

For example,
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.
Return the formatted lines as:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
==================================
Worked on this problem before https://github.com/lijenpan/python/blob/master/rackspace/q2/solution.py.
But let's solve this without using libraries, which is hard.

Turns out that this is also a DP problem: https://www.youtube.com/watch?v=ENyox7kNKeY
"""


def fullJustify(words, L):
    """
    :type words: List[str]
    :type L: int
    :rtype: List[str]
    """
    res = []
    i = 0
    while i < len(words):
        size = 0
        begin = i
        while i < len(words):
            newsize = len(words[i]) if size == 0 else size + len(words[i]) + 1
            if newsize <= L:
                size = newsize
            else:
                break
            i += 1
        spaceCount = L - size
        if i - begin - 1 > 0 and i < len(words):
            everyCount = spaceCount / (i - begin - 1)
            spaceCount %= i - begin - 1
        else:
            everyCount = 0
        j = begin
        while j < i:
            if j == begin:
                s = words[j]
            else:
                s += ' ' * (everyCount + 1)
                if spaceCount > 0 and i < len(words):
                    s += ' '
                    spaceCount -= 1
                s += words[j]
            j += 1
        s += ' ' * spaceCount
        res.append(s)
    return res
