#!/usr/bin/python3
"""base module"""
import json
import turtle
import csv


class Base:
    """class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                m = [p.to_dictionary() for p in list_objs]
                f.write(Base.to_json_string(m))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            else:
                dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".json"
        m = []
        try:
            with open(filename, "r") as f:
                listObj = cls.from_json_string(f.read())
                for dic in listObj:
                    m.append(cls.create(**dic))
                return m
        except Exception:
            return m

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes in CSV"""
        filename = cls.__name__ + ".csv"
        if list_objs is not None:
            with open(filename, "w") as f:
                m = csv.writer(f)
                for j in list_objs:
                    if cls.__name__ == "Square":
                        m.writerow([j.id, j.width, j.x, j.y])
                    if cls.__name__ == "Rectangle":
                        m.writerow([j.id, j.width, j.height, j.x, j.y])
        else:
            with open(filename, "w") as f:
                f.write("[]")

    @classmethod
    def load_from_file_csv(cls):
        """deserializes in CSV"""
        filename = cls.__name__ + ".csv"
        obj = []
        with open(filename, "r", newline='') as f:
            read = csv.reader(f)
            for row in read:
                if cls.__name__ == "Square":
                    d = {"id": int(row[0]),
                         "size": int(row[1]),
                         "x": int(row[2]),
                         "y": int(row[3])}
                if cls.__name__ == "Rectangle":
                    d = {"id": int(row[0]),
                         "width": int(row[1]),
                         "height": int(row[2]),
                         "x": int(row[3]),
                         "y": int(row[4])}
                create = cls.create(**d)
                obj.append(create)
        return obj

    @classmethod
    def draw(list_rectangles, list_squares):
        """opens a window and draws all the Rectangles and Squares"""
        figure = turtle.Turtle()
        figure.pensize(4)
        figure.color("#827bbe")
        figure.shape("turtle")
        figure.hideturtle()
        allfig = list_rectangles + list_squares

        for cre in allfig:
            figure.showturtle()
            figure.up()
            figure.goto(cre.x, cre.y)
            figure.down()
            figure.forward(cre.width)
            figure.left(90)
            figure.forward(cre.height)
            figure.left(90)
            figure.forward(cre.width)
            figure.left(90)
            figure.forward(cre.height)
            figure.left(90)

        turtle.exitonclick()
