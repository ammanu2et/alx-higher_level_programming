#!/usr/bin/python3
"""Square is an empty class that defines a square."""


class Square:
    """Empty class Square that defines a square.

    args size (int):
        The size of a square is crucial for a square,
        many things depend of it (area computation, etc.), so you,
        as class builder, must control the type and value of this attribute.

    Attributes:
        The size of a square is crucial for a square,
        many things depend of it (area computation, etc.), so you,
        as class builder, must control the type and value of this attribute.

    """

    def __init__(self, size=0):
        self.__size = size

    """ """

    def size(self):
        if size < 0
            return "size must be >= 0"
        if int(size):
            return self.size = size
        else:
            return "size must be an integer"
