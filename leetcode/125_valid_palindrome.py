"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.
===============================
If you have solved other palidrome problems. This is super simple.
"""


def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    new_s = [c.lower() for c in s if c.isalnum()]
    return new_s == new_s[::-1]
