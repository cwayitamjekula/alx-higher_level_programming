#!/usr/bin/python3

"""Creating rectangle class"""


class Rectangle:
    """rectangle class"""
     def __init__(self, width=0, height=0):
        """Initialize class."""
        self.width = width
        self.height = height

    @property
    def height(self):
        """To get height."""
        return self.__height

    @height.setter
    def height(self, value):
        """To set height."""
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    @property
    def width(self):
        """To get width."""
        return self.__width

    @width.setter
    def width(self, value):
        """To set width."""
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value
