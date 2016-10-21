"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".
==============================
Wish I had a brain like his: https://discuss.leetcode.com/topic/43463/1-2-lines-python-ruby
"""

import re


def reverseVowels(s):
    """
    :type s: str
    :rtype: str
    """
    vowels = re.findall('(?i)[aeiou]', s)
    return re.sub('(?i)[aeiou]', lambda m: vowels.pop(), s)
