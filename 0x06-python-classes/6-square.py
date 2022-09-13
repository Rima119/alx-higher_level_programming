#!/usr/bin/python3
"""Square Class"""


class Square:
    """class Square that defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """
            Instantiation with size
        Args:
            size: size of a square
            position: position of a square
        """
        self.__size = size
        self.position = position

    def area(self):
        """Returns the current square area"""
        return (self.__size * self.__size)

    @property
    def size(self):
        """Returns size"""
        return self.__size

    @size.setter
    def size(self, size):
        """Set size"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def position(self):
        """Returns position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set position"""
        if type(value) != tuple or len(value) != 2 or \
           not isinstance(value[0], int) or \
           not isinstance(value[1], int) or \
           value[0] < 0 or value[1]:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        for n in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
        for m in range(self.__position[1]):
            print()
