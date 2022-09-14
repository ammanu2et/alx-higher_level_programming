#!/usr/bin/python3
""" class Square that defines a square"""


class Square:
    """ class Square that defines a square"""

    def __init__(self, size=0):
        """initialize square
        Args:
            value (int): size of the square
        """
        self.__size = size

    @property
    def size(self):
        """int: size
        Returns:
            size (int): size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """int: sets value into size

        Args:
            value (int): size of the square.
        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """initialize area
            Returns:
            area (int): area of the square
        """
        return self.__size ** 2
