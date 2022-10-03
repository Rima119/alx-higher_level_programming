#!/usr/bin/python3
"""Unittests for base
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
import pep8
import os
from io import StringIO
from unittest import TestCase


class TestBase(unittest.TestCase):
    """Test Cases"""
    def setUp(self):
        Base._Base__nb_objects = 0
