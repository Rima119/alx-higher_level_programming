#!/usr/bin/python3
import math

"""MagicClass Class"""


class MagicClass:
    """class that does exactly the same as the following Python bytecode"""
    def __init__(self, radius=0):
        self.__radius = 0
        if type(radius) != int and type(radius) != float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        return ((self.__radius * self.__redius) * math.pi)

    def circumference(self):
        return (2 * math.pi * self.__radius)
