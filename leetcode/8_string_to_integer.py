"""
Implement atoi to convert a string to an integer.

Hint:
Requirements for atoi:
The function first discards as many whitespace characters as necessary until the first non-whitespace character is
found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical
digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have
no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence
exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of
representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.
"""


def myAtoi(str):
    """
    :type str: str
    :rtype: int
    """
    INT_MAX = 2147483647
    INT_MIN = -2147483648
    my_sum = 0
    sign = 1
    i = 0
    if str == '':
        return 0
    while i < len(str) and str[i].isspace():
        i += 1
    if i < len(str) and str[i] == '-':
        sign = -1
    if i < len(str) and (str[i] == '-' or str[i] == '+'):
        i += 1
    while i < len(str) and str[i].isdigit():
        digit = int(str[i])
        if INT_MAX / 10 >= my_sum:
            my_sum *= 10
        else:
            if sign == 1:
                return INT_MAX
            else:
                return INT_MIN
        if INT_MAX - digit >= my_sum:
            my_sum += digit
        else:
            if sign == 1:
                return INT_MAX
            else:
                return INT_MIN
        i += 1
    return sign * my_sum
