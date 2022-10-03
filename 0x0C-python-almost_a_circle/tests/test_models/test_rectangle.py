#!/usr/bin/python3
"""Unittest Rectangle"""
import unittest
from models.rectangle import Rectangle
from models.base import Base
import pep8
from io import StringIO
from unittest import TestCase
import os


class TestRectangle(unittest.TestCase):
    """Test Cases"""
    def setUp(self):
        Base._Base__nb_objects = 0

    def new_rectangle(self):
        self.setUp()
        r1 = Rectangle(10, 2)
        r1.id = 1
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(2, 10)
        r2.id = 2
        self.assertEqual(r2.id, 2)
        r3 = Rectangle(10, 2, 0, 0, 12)
        r3.id = 12
        self.assertEqual(r3.id, 12)
