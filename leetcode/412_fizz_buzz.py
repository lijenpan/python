"""
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output "Fizz" instead of the number and for the multiples of five output "Buzz".
For numbers which are multiples of both three and five output "FizzBuzz".

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
==============================
You can't fail this one.
"""


def fizzBuzz(n):
    """
    :type n: int
    :rtype: List[str]
    """
    res = []
    for x in xrange(1, n + 1):
        if x % 15 == 0:
            res.append("FizzBuzz")
        elif x % 3 == 0:
            res.append("Fizz")
        elif x % 5 == 0:
            res.append("Buzz")
        else:
            res.append(str(x))
    return res
