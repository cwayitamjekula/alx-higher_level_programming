#!/usr/bin/python3

"""Creating rectangle class"""

class Rectangle:
        """rectangle class
    
           Attributes:
            width: A private instance with optional type
            height: A private instance with optional type

    """
    number_of_instances = 0
    print_symbol = '#'
    def __init__(self, width=0, height=0):
        """Initialize class."""
        self.width = width
        self.height = height
   
        """
        checking if height and width are integers

        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

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

    @property
    def height(self):
        """To get height."""
        return self.__height

    @height.setter
    def height(self, value):
        """To set height."""
        if type(value) != int:
            raise TypeErroe('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Returns area."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Returns the rectangle with the character #."""
        str_result = ""
        if self.__width == 0 or self.__height == 0:
            return str_result
        for row in range(self.__height):
            for col in range(self.__width):
                str_result += str(self.print_symbol)
            if row < self.__height - 1:
                str_result += '\n'
        return str_result

    def __repr__(self):
        """Returns string representation of the rectangle"""
        return 'Rectangle(%s, %s)' % (self.__width, self.__height)

    def __del__(self):
        """Prints a message when the rectangle is deleted"""
        type(self).number_of_instances -= 1
        print('Bye rectangle...')
