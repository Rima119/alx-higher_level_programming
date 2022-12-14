#!/usr/bin/python3
"""Rectangle module"""
from models.base import Base


class Rectangle(Base):
    """class Rectangle that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize a rectangle object"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """get the width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width of rectangle"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """get the height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height of rectangle"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """get the x coordinate of rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """set the x coordinate of rectangle"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """get the y coordinate of rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """set the y coordinate of rectangle"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """return the area of rectangle"""
        return self.width * self.height

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        m = self.y * "\n"
        for k in range(self.height):
            m += (" " * self.x)
            m += ("#" * self.width) + "\n"
        print(m, end='')

    def __str__(self):
        """returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return ("[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """assigns a key/value argument to attributes"""
        if args:
            for kv in range(len(args)):
                if kv == 0:
                    self.id = args[kv]
                if kv == 1:
                    self.__width = args[kv]
                if kv == 2:
                    self.__height = args[kv]
                if kv == 3:
                    self.__x = args[kv]
                if kv == 4:
                    self.__y = args[kv]
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        return {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
                }
