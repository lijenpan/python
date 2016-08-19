"""
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
Return:

[
  ["ate", "eat", "tea"],
  ["nat", "tan"],
  ["bat"]
]
==================================
First thing comes to mind is do permutations since anagram is just re-arranging letters in a word.
But we can cheat by sort each word and find matches.

But this is considered too slow:
def groupAnagrams(strs):
    groups = []
    for s in strs:
        base_word = ''.join(sorted(s))
        matches = [a for a in strs if base_word == ''.join(sorted(a))]
        if matches not in groups:
            groups.append(matches)
    return groups
"""


def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    dict = {}
    for word in strs:
        sortedword = ''.join(sorted(word))
        dict[sortedword] = [word] if sortedword not in dict else dict[sortedword] + [word]
    res = []
    for item in dict:
        if len(dict[item]) >= 1:
            res.append(dict[item])
    return res
