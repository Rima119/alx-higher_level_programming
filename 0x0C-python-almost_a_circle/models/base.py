#!/usr/bin/python3
"""models/base.py"""
import json
import turtle
import csv


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        a = []
        if list_objs is not None:
            for k in list_objs:
                a.append(cls.to_dictionary(k))
        with open(filename, 'w') as file:
            file.write(cls.to_json_string(a))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ is "Rectangle":
            m = cls(1, 1)
        elif cls.__name__ is "Square":
            m = cls(1)
        m.update(**dictionary)
        return m
