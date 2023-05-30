#!/usr/bin/python3
 """ square class """

class Square():
    """ square class wit private attribute"""
    
    def __init__(self, size=0):
        """size is a private attribute"""
        self.__size = size
        
        if type(size) is not int:
            raise TypeError("make sure size is an integer")
        if size < 0:
            raise ValueError("size can not be negative")
        self.__size = size

        """ area of square """
        def area(self):  
            return (self.__size * self.__size)

        @property
        def size(self):
            """Handling size errors """
            return self.__size

        @size.setter
        def size(self, value):
            """Set square size """

            if type(value) is not int:
                raise TypeError("make sure size is an integer")
            if value < 0:
                raise ValueError("size can not be negative")
            self.__size = value

            def my_print(self):
                """Printing square with # """
                if self.__size == 0:
                    print()
                else:
                    for row in range(self.__size):
                        for column in range(self.__size):
                            print("#", end="")
                            print()
