"""
Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
Note: It is intended for the problem statement to be ambiguous. You should gather all requirements
up front before implementing one.

Update (2015-02-10):
The signature of the C++ function had been updated. If you still see your function signature accepts
a const char * argument, please click the reload button  to reset your code definition.
==================================
Not a very good question for leetcode then since we have no one to ask.
Nevertheless, I don't think this is hard.
"""


def isNumber(s):
    """
    :type s: str
    :rtype: bool
    """
    try:
        float(s)
    except:
        return False
    else:
        return True
