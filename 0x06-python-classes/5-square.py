#!/usr/bin/python3
"""Square class"""


class Square():
    """Square class with private instance attribute size and raise errors
       and public instance method area and getter and setter
       and public instance method my_print"""
    def __init__(self, size=0):
        """__init__ method
        Args:
            size (int): size of square
        """
        self.__size = size

    @property
    def size(self):
        """size getter
        Returns:
            int: size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """size setter
        Args:
            value (int): size of square
        """
        self.__size = value
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """area method
        Returns:
            int: area of square
        """
        return self.__size * self.__size

    def my_print(self):
        """my_print method
        Returns:
            prints square
        """
        if self.__size == 0:
            print('')
        else:
            n = 0
            while n < self.__size:
                i = 0
                while i < self.__size:
                    print('#', end='')
                    i += 1
                print()
                n += 1
