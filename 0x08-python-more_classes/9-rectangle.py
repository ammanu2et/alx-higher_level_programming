#!/usr/bin/python3
""" empty class Rectangle that defines a rectangle
"""


class Rectangle:
    """ class rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Instantiation with optional width and height"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """ width
        """
        return self.__width

    @property
    def height(self):
        """height
        """
        return self.__height

    @width.setter
    def width(self, value):
        """ width setter
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """ height setter
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError('rect_1 must be an instance of Rectangle')
        elif type(rect_2) is not Rectangle:
            raise TypeError('rect_2 must be an instance of Rectangle')
        else:
            return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    @classmethod
    def square(cls, size=0):
        """a class method that returns the size of the rectangle."""
        return Rectangle(size, size)

    def area(self):
        """initialize area
        Returns:
            area (int):
        """
        return (self.__height * self.__width)

    def perimeter(self):
        """perimeter
            Returns: the perimeter of a rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * (self.__width + self.__height))

    def __str__(self):
        """Print the rectangle with the # character."""
        if self.__height == 0 or self.__width == 0:
            return ""

        return ("\n".join(["".join([str(self.print_symbol)
                for i in range(self.__width)])for j in range(self.__height)]))

    def __repr__(self):
        """Returns the string representation of the function."""
        return 'Rectangle({}, {})'.format(self.__width, self.__height)

    def __del__(self):
        """Delete the rectangle."""
        type(self).number_of_instances -= 1
        print('Bye rectangle...')
