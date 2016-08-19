"""
Implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "*") → true
isMatch("aa", "a*") → true
isMatch("ab", "?*") → true
isMatch("aab", "c*a*b") → false
==================================
Ok, let's solve this one for real without cheating. Without using re, this is a hard problem.

Here is a pseudo code:
for each element in s:
    if s == p or p == ?, this is a match, move index.
    if p == "*" this is a match, we need keep track where "*" appears and last matched position.
    if not a match, then check if there is a "*" showed up,
        if no, return false
        else, we set current pointer to "*" index + 1, and second pointer to last matched position.

Now we just need to code it up!
"""


def isMatch(s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    p_index = 0
    s_index = 0
    ss = 0
    start = -1
    while s_index < len(s):
        if p_index < len(p) and (s[s_index] == p[p_index] or p[p_index] == '?'):
            p_index += 1
            s_index += 1
            continue
        if p_index < len(p) and p[p_index] == '*':
            start = p_index
            p_index += 1
            ss = s_index
            continue
        if start != -1:
            p_index = start + 1
            ss += 1
            s_index = ss
            continue
        return False
    while p_index < len(p) and p[p_index] == '*':
        p_index += 1
    if p_index == len(p):
        return True
    return False
