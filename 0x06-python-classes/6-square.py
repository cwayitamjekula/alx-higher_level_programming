#!/usr/bin/python3
"""Square class"""

class Square():
    """Square class with private instance attribute """
    def __init__(self, size=0, position=(0, 0)):
        """
        Args:
            size (int): size of square
            position (tuple): position of square
        """
        self.__size = size
        self.__position = position
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")
        try:
            if not isinstance(position, tuple):
                raise TypeError
            if len(position) != 2:
                raise TypeError
            if not isinstance(position[0], int):
                raise TypeError
            if not isinstance(position[1], int):
                raise TypeError
            if position[0] < 0 or position[1] < 0:
                raise TypeError
        except TypeError:
            raise TypeError("position must be a tuple of 2 positive integers")

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
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        """
        Returns:
            tuple: position of square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Args:
            value (tuple): position of square
        """
        try:
            if not isinstance(value, tuple):
                raise TypeError
            if len(value) != 2:
                raise TypeError
            if not isinstance(value[0], int):
                raise TypeError
            if not isinstance(value[1], int):
                raise TypeError
            if value[0] < 0 or value[1] < 0:
                raise TypeError
            self.__position = value
        except TypeError:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """
        Returns:
            int: area of square
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Returns:
            prints square
        """
        n = 0
        if self.__size == 0:
            print()
        else:
            while n < self.__position[1]:
                print()
                n += 1
            i = 0
            while i < self.__size:
                k = 0
                x = 0
                while k < self.__position[0]:
                    print(' ', end='')
                    k += 1
                while x < self.__size:
                    print('#', end='')
                    x += 1
                print()
                i += 1
