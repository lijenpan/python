"""
Compare two version numbers version1 and version2.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of
the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 13.37
===============================
So many edge cases.
"""


def compareVersion(version1, version2):
    """
    :type version1: str
    :type version2: str
    :rtype: int
    """
    v1 = version1.split('.')
    v2 = version2.split('.')
    min_len = min(len(v1), len(v2))
    for i in xrange(min_len):
        if int(v1[i]) > int(v2[i]):
            return 1
        elif int(v1[i]) < int(v2[i]):
            return -1

    if len(v1) > len(v2):
        for x in v1[min_len:]:
            if int(x) != 0:
                return 1
    if len(v1) < len(v2):
        for x in v2[min_len:]:
            if int(x) != 0:
                return -1
    return 0
