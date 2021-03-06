#!/usr/bin/python3
"""Simple Square class"""


class Square:
    """Simple class with attrs validation.
    Args:
        size (int): Size of the square
    Raises:
        TypeError: If size type is not int
        ValueError: If size < 0
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """Method to calculate the area of the square.
        """
        return self.__size ** 2
