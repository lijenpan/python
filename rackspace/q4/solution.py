from UserString import MutableString


def strip_whitespace_and_adjacent_duplicate_letter(text):
    """This is purely for the sake of the exercise because MutableString
    is deprecated in Python 3. The proper solution still needs to be in
    C/C++.

    >>> strip_whitespace_and_adjacent_duplicate_letter("abb cddpddef gh")
    'abcdpdefgh'

    >>> strip_whitespace_and_adjacent_duplicate_letter("aaaadam mmmm")
    'adam'
    """
    mutable_text = MutableString(text)
    num_of_whitespace = mutable_text.count(' ')

    for i in xrange(0, num_of_whitespace):
        mutable_text.remove(' ')
    
    mutable_text_length = len(mutable_text)
    i = 0
    
    while i < mutable_text_length - 1:
        if mutable_text[i] == mutable_text[i + 1]:
            del mutable_text[i + 1]
            mutable_text_length -= 1
            i = 0
        else:
            i += 1
    return mutable_text

if __name__ == '__main__':
    import doctest
    doctest.testmod()
