"""
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
==================================
This is easy in Python.
"""


def simplifyPath(path):
    """
    :type path: str
    :rtype: str
    """
    path = path.split('/')
    curr = '/'
    for i in path:
        if i == '..':
            if curr != '/':
                curr = '/'.join(curr.split('/')[:-1])
                if curr == '': curr = '/'
        elif i != '.' and i != '':
            curr += '/' + i if curr != '/' else i
    return curr


if __name__ == "__main__":
    assert simplifyPath("/a/./b///../c/../././../d/..//../e/./f/./g/././//.//h///././/..///") == "/e/f/g"
    assert simplifyPath("/a/./b/../../c/") == "/c"
    assert simplifyPath("/home/") == "/home"
    assert simplifyPath("/../") == "/"
    assert simplifyPath("/home//foo/") == "/home/foo"
    assert simplifyPath("/...") == "/..."
