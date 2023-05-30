#!/usr/bin/python3
"""Square class"""


class Square():
    """Square class with private instance attribute"""
    def __init__(self, size=0):
        """ Args:
            size (int): size of square
        """
        self.__size = size
