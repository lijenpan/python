"""Write a method that converts its argument from integer to roman numeral if
a numeric value is passed, or from roman numeral to an integer if a roman numeral is passed.
Your solution should rely on the parameter's class to determine its type and if a non-roman numeral character
is passed (i.e. 'M3I',) the method should raise a BadRomanNumeral exception.

The solution should be a single method that accepts a single argument and return the converted value.
Additionally, your solution should demonstrate your mastery of Python's exception handling capabilities.

Include unit tests to verify correct conversion of both types of input, and verify exception
output with bad input.
"""

import re

class RomanError(Exception): pass
class OutOfRangeError(RomanError): pass
class NotIntegerError(RomanError): pass
class BadRomanNumeral(RomanError): pass

romanNumeralMap = (('M',  1000),
                   ('CM', 900),
                   ('D',  500),
                   ('CD', 400),
                   ('C',  100),
                   ('XC', 90),
                   ('L',  50),
                   ('XL', 40),
                   ('X',  10),
                   ('IX', 9),
                   ('V',  5),
                   ('IV', 4),
                   ('I',  1))

# Define pattern to detect valid Roman numerals
romanNumeralPattern = re.compile("""
    ^                   # beginning of string
    M{0,4}              # thousands - 0 to 4 M's
    (CM|CD|D?C{0,3})    # hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 C's),
                        #            or 500-800 (D, followed by 0 to 3 C's)
    (XC|XL|L?X{0,3})    # tens - 90 (XC), 40 (XL), 0-30 (0 to 3 X's),
                        #        or 50-80 (L, followed by 0 to 3 X's)
    (IX|IV|V?I{0,3})    # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 I's),
                        #        or 5-8 (V, followed by 0 to 3 I's)
    $                   # end of string
    """, re.VERBOSE)


def integer_roman_numeral_convertor(a):
    """If the input is an integer, try to convert it to Roman numeral.
    Otherwise try to convert it to integer.

    >>> integer_roman_numeral_convertor(1)
    'I'

    >>> integer_roman_numeral_convertor(100)
    'C'

    >>> integer_roman_numeral_convertor(4999)
    'MMMMCMXCIX'

    >>> integer_roman_numeral_convertor(5000)
    Traceback (most recent call last):
    ...
    OutOfRangeError: numer out of range (must be between 1 and 4999)

    >>> integer_roman_numeral_convertor('MMMMCMXCIX')
    4999

    >>> integer_roman_numeral_convertor('C')
    100

    >>> integer_roman_numeral_convertor('I')
    1

    >>> integer_roman_numeral_convertor('A')
    Traceback (most recent call last):
    ...
    BadRomanNumeral: Invalid Roman numeral: A

    >>> integer_roman_numeral_convertor('A')
    Traceback (most recent call last):
    ...
    BadRomanNumeral: Invalid Roman numeral: A

    >>> integer_roman_numeral_convertor('M3I')
    Traceback (most recent call last):
    ...
    BadRomanNumeral: Invalid Roman numeral: M3I
    """
    if type(a) == int:
        return toRoman(a)
    else:
        return fromRoman(a)


def toRoman(n):
    """convert integer to Roman numerals."""
    if not (0 < n < 5000):
        raise OutOfRangeError, "numer out of range (must be between 1 and 4999)"

    if int(n) != n:
        raise NotIntegerError, "decimals cannot be converted."

    result = ""
    for numeral, integer in romanNumeralMap:
        while n >= integer:
            result += numeral
            n -= integer
    return result


def fromRoman(s):
    """convert Roman numeral to integer."""
    if not s:
        raise BadRomanNumeral, "Input cannot be blank"
    if not romanNumeralPattern.search(s):
        raise BadRomanNumeral, "Invalid Roman numeral: %s" % s

    result = 0
    index = 0
    for numeral, integer in romanNumeralMap:
        while s[index:index + len(numeral)] == numeral:
            result += integer
            index += len(numeral)
    return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()