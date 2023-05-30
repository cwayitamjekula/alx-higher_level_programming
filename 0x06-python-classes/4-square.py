#!/usr/bin/python3
"""Square class"""


class Square():
    """Square class with private instance attribute"""
    def __init__(self, size=0):
        """
        Args:
            size (int): size of square
        """
        self.__size = size

    @property
    def size(self):
        """
        Returns:
            int: size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Args:
            value (int): size of square
        """
        self.__size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        Returns:
            int: area of square
        """
        return self.__size * self.__size
