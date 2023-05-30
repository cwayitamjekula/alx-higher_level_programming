#!/usr/bin/python3
 """ square class """

class Square():
    """ square class wit private attribute"""
    
    def __init__(self, size=0):
        """size is a private attribute
        position: postion of the square """
        self.__size = size  
        if type(size) is not int:
            raise TypeError("make sure size is an integer")
        if size < 0:
            raise ValueError("size can not be negative")
        self.__size = size
        self.position = position

        def area(self):
            """area of the square"""
            return (self.__size * self.__size)

        @property
        def size(self):
            """ get size of square"""
            return self.__size

        @size.setter
        def size(self, value):
            """set square size """
            if type(value) is not int:
                raise TypeError("make sure size is an integer")
            if value < 0:
                raise ValueError("size can not be negative")
            self.__size = value

            def my_print(self):
                """Print a square with  # at set position"""
                if self.__size == 0:
                    print()
                    return
                for i in range(self.__position[1]):
                    print()
                    for n in range(self.__size):
                        print(" " * self.__position[0], end="")
                        print("#" * self.__size)

                        @property
                        def position(self):
                            """ set position of square """
                            return self.__position

                        @position.setter
                        def position(self, value):
                            
                            if type(value) != tuple:
                                raise TypeError("position must be a tuple of 2 positive numbers")
                            elif len(value) != 2:
                                raise TypeError("position must be a tuple of 2 positive numbers")
                            elif isinstance(value[0], int) is False:
                                raise TypeError("position must be a tuple of 2 positive numbers")
                            elif isinstance(value[1], int) is False:
                                raise TypeError("position must be a tuple of 2 positive numbers")
                            elif value[0] < 0 or value[1] < 0:
                                raise TypeError("position must be a tuple of 2 positive numbers")
                            else:
                                self.__position = value
