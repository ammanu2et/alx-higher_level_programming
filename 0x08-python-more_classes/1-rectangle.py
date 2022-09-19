#!/usr/bin/python3
"""empty class Rectangle that define a rectangle.
"""


class Rectangle:
    """Rectangel class that defines a rectangle."""
    def __init__(self, width=0, height=0):
        """Initialize Rectangel
        Args:
            width (int): width of the rectangle.
            height (int): the height of the rectangle.
        """
        self.width = width
        self.height = height

    @proprty
    def width(self):
        """int: private width
        Returns:
            private width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        width setter
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """int: private height
        Returns:
            private height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        height setter
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
