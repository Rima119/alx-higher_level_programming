#!/usr/bin/python3
"""Rectangle Class"""


class Rectangle:
    """an empty class that defines a rectangle"""
    def __init__(self, width=0, height=0):
        """
        Instantiation with optional width and height

        Args:
            width: width of the rectangle (integer)
            height: height of the rectangle (integer)
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the rectangle area"""
        return self.width * self.height

    def perimeter(self):
        """returns the rectangle perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        return (2 * self.width) + (2 * self.height)

    def __str__(self):
        """print the rectangle with the character #"""
        txt = ""
        if self.__height == 0 or self.width == 0:
            return txt
        for n in range(self.__height - 1):
            txt += "#" * self.__width + "\n"
        txt += "#" * self.__width
        return txt

    def __repr__(self):
        """return a string representation of the rectangle"""
        return "Rectangle({:d}, {:d})".format(self.width, self.height)
