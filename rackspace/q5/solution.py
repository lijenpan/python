def print_2d_array_clockwise(two_d_array):
    """
    >>> print_2d_array_clockwise([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    [1, 2, 3, 6, 9, 8, 7, 4, 5]

    >>> print_2d_array_clockwise([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
    """

    return list(two_d_array[0])\
        + print_2d_array_clockwise(list(reversed(zip(*two_d_array[1:]))))\
        if two_d_array else []


if __name__ == '__main__':
    import doctest
    doctest.testmod()