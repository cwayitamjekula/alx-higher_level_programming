#!/usr/bin/python3
 """ square class """

class Square():
    """ square class wit private attribute"""
    
    def __init__(self, size=0):
        """size is a private attribute"""
        self.__size = size
        
    @property
    def size(self):
        """get the size of the square"""
        return (self.__size)
     """ set size of square """
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("make sure size is an integer")
        elif value < 0:
            raise ValueError("size can not be negative")
        else:
            self.__size = value

    def area(self):
        return (self.__size * self.__size)