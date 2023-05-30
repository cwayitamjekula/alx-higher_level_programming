#!/usr/bin/python3
 """ square class """

class Square():
    """ square class wit private attribute"""
    
    def __init__(self, size=0):
        """size is a private attribute"""
        self.__size = size
        
        if size != int(size):
            raise TypeError("make sure size is an integer")
        if size < 0:
            raise ValueError("size can not be negative")
        self.__size = size

    def area(self):
        """returning area of the square"""
        return (self.__size ** 2)
