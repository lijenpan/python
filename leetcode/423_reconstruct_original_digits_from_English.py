"""
Given a non-empty string containing an out-of-order English representation of digits 0-9, output the digits in ascending order.

Note:
Input contains only lowercase English letters.
Input is guaranteed to be valid and can be transformed to its original digits. That means invalid inputs such as "abc" or "zerone" are not permitted.
Input length is less than 50,000.
Example 1:
Input: "owoztneoer"

Output: "012"
Example 2:
Input: "fviefuro"

Output: "45"
==============================
First thing comes to mind is to brutal force it since there are only 10 digits. But since the input string is guaranteed
to be correctly spelled, we can start counting unique letter in each word. For example, "z" only appears in zero.
"""
from collections import Counter


def originalDigits(s):
    """
    :type s: str
    :rtype: str
    """
    char_counter = Counter(s)
    digit_counter = {}
    for char, count in char_counter.iteritems():
        digit_counter[0] = char_counter['z']
        digit_counter[2] = char_counter['w']
        digit_counter[4] = char_counter['u']
        digit_counter[6] = char_counter['x']
        digit_counter[8] = char_counter['g']
        digit_counter[3] = char_counter['h'] - digit_counter[8]
        digit_counter[5] = char_counter['f'] - digit_counter[4]
        digit_counter[7] = char_counter['s'] - digit_counter[6]
        digit_counter[1] = char_counter['o'] - digit_counter[0] - digit_counter[2] - digit_counter[4]
        digit_counter[9] = char_counter['i'] - digit_counter[5] - digit_counter[6] - digit_counter[8]
    return ''.join(str(digit) * count for digit, count in digit_counter.iteritems())
