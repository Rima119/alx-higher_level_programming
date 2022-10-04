#!/usr/bin/python3
"""square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """return [Square] (<id>) <x>/<y> - <size>"""
        return ("[Square] ({:d}) {:d}/{:d} - {:d}"
                .format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """get the size of square"""
        return self.width

    @size.setter
    def size(self, value):
        """set the size of square"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns attributes"""
        if args:
            for kv in range(len(args)):
                if kv == 0:
                    self.id = args[kv]
                if kv == 1:
                    self.size = args[kv]
                if kv == 2:
                    self.x = args[kv]
                if kv == 3:
                    self.y = args[kv]
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        return {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
                }
