#!/usr/bin/python3
"""Unittsets for base_model.py"""


import datetime
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test BaseModel class"""
    def test_isoformat(self):
        """test isoformat of datettime"""
        now = datetime.datetime(2023, 4, 6, 18, 25, 31, 92221)
        self.assertEqual(now.isoformat(), '2023-04-06T18:25:31.092221')
