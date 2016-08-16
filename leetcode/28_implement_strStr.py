"""
Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
======================
Are you kidding me??!!
"""


def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    if len(needle) > len(haystack):
        return -1
    try:
        return haystack.index(needle)
    except ValueError:
        return -1
