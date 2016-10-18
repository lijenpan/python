"""
Given an arbitrary ransom note string and another string containing letters from all the magazines,
write a function that will return true if the ransom note can be constructed from the magazines;
otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
==============================
Okay. This is dumb.
"""

from collections import Counter

def canConstruct(ransomNote, magazine):
    """
    :type ransomNote: str
    :type magazine: str
    :rtype: bool
    """
    r_counter = Counter(ransomNote)
    m_counter = Counter(magazine)
    for k, v in r_counter.iteritems():
        if m_counter[k] < v:
            return False
    return True
