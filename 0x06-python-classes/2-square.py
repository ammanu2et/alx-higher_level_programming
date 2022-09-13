#!/usr/bin/python3
"""class square defines a square."""


class Square:
    """Empty class Square that defines a square.

    args size (int):
        The size of a square is crucial for a square,
        many things depend of it (area computation, etc.), so you,
        as class builder, must control the type and value of this attribute.

    """

    def __init__(self, size=0):

    """ Attributes:
        The size of a square is crucial for a square,
        many things depend of it (area computation, etc.), so you,
        as class builder, must control the type and value of this attribute.
    """

        if size < 0:
            raise ValueError('size must be >= 0')
        elif type(size) is not int:
            raise TypeError('size must be an integer')
        else:
            self.__size = size
