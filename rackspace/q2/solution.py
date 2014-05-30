import textwrap


def justify(width, text):
    """
    >>> justify(20, "The quick brown fox jumps over the lazy dog.")
    The  quick brown fox
    jumps  over the lazy
    dog.

    >>> justify(20, "The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog.")
    The  quick brown fox
    jumps  over the lazy
    dog. The quick brown
    fox  jumps  over the
    lazy  dog.

    >>> justify(30, "The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog.")
    The quick brown fox jumps over
    the  lazy dog. The quick brown
    fox  jumps  over the lazy dog.
    """

    for line in textwrap.wrap(text, width):
        padding = width - len(line)
        print line.replace(" ", "  ", padding)


if __name__ == '__main__':
    import doctest
    doctest.testmod()