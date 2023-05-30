#!/usr/bin/python3
 """ square class """
class Square():
    """ size set as a private attribute """
    def __init__(self, size=0):
        """ size: size of the square """
       self.__size = size
        if type(size) is not int:
            raise TypeError("make sure size is an integer")
        if size < 0:
            raise ValueError("size can not be a negative number")
