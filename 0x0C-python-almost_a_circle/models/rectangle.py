#!/usr/bin/python3
"""Module that defines rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Represent a rectrangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a rectangle
        width (int): the width of rectangle.
        height (int): the height of rectangle.
        x (int): the x coordinate of the rectangle.
        y (int): the y coordinate of the rectangle.
        id (int): the identity of rectangle.

        Raises:
            TypeError: If either of width or height is not an integer.
            ValueError: If either of width or height <= 0.
            TypeError: If either x or y is not an int.
            ValueError: if either x or y < 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """set/get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """set/get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer.")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """set/get the x coordinate of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """set/get the y coordinate of rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value


