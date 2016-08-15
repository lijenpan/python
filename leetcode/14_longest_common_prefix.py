"""
Write a function to find the longest common prefix string amongst an array of strings.
"""


def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if len(strs) == 0:
        return ""
    if len(strs) == 1:
        return strs[0]
    min_length = min(len(s) for s in strs)
    if min_length == 0:
        return ""
    for i in xrange(0, min_length):
        prefixes = [x[:i+1] for x in strs]
        if len(set(prefixes)) != 1:
            return prefixes[0][:i]
    return prefixes[0]
