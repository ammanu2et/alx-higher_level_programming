#!/usr/bin/python3
""" class Square that defines a square"""


class Square:
    """ class Square that defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """initialize square
        Args:
            size (int): size of the square.
            position (int, int): the position of the square.
        """
        self.__size = size
        self.position = position

    @property
    def size(self):
        """int: private size
        Returns:
            Private size.
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
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    @property
    def position(self):
        """int: private position
            Returns:
                private position.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """tuple of 2 positive int:

        Args:
            value (int): position of the square.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(num, int) for num in value) or not all(num >= 0 for num in value)):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """initialize area
            Returns:
            area (int): area of the square
        """
        return (self.__size * self.__size)

    def my_print(self):
        """to print the square.
            Returns:
            the stdout square with char #.
        """
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print('#', end="") for k in range(0, self.__size)]
            print("")
