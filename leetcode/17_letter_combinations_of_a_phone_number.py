"""
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
=================================
I think I solved this problem before... Leetcode doesn't allow itertools even though the problem statement states
no such constraint...
"""
MAPPING = {
    "1": "",
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
    "0": " "
}


def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    if '' == digits:
        return []
    return reduce(lambda acc, digit: [x + y for x in acc for y in MAPPING[digit]], digits, [''])
