"""
You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

For example, given:
s: "barfoothefoobarman"
words: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).
=====================================
The code can be a lot shorter with itertools.permutations.
"""
import itertools


def findSubstring(s, words):
    """
    :type s: str
    :type words: List[str]
    :rtype: List[int]
    """
    hash = {}
    res = []
    wsize = len(words[0])

    for str in words:
        if str in hash:
            hash[str] += 1
        else:
            hash[str] = 1
    for start in range(0, len(words[0])):
        slidingWindow = {}
        wCount = 0
        for i in range(start, len(s), wsize):
            word = s[i: i + wsize]
            if word in hash:
                if word in slidingWindow:
                    slidingWindow[word] += 1
                else:
                    slidingWindow[word] = 1
                wCount += 1
                while hash[word] < slidingWindow[word]:
                    pos = i - wsize * (wCount - 1)
                    removeWord = s[pos: pos + wsize]
                    slidingWindow[removeWord] -= 1
                    wCount -= 1
            else:
                slidingWindow.clear()
                wCount = 0
            if wCount == len(words):
                res.append(i - wsize * (wCount - 1))

    return res
