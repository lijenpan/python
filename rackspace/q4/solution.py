import re
import UserString


def strip_whitespace_and_adjacent_duplicate_letter(text):
    """Returns string without whitespace and with
    duplicate characters if they are next to each other.

    >>> strip_whitespace_and_adjacent_duplicate_letter("abb cddpddef gh")
    'abcdpdefgh'

    >>> strip_whitespace_and_adjacent_duplicate_letter("aaaadam mmmm")
    'adam'
    """
    mutable_text = UserString.MutableString(text)
    return re.sub(r'([a-z])\1+', r"\1", ''.join(mutable_text.split()))


if __name__ == '__main__':
    import doctest
    doctest.testmod()