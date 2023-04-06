#!/usr/bin/python3
"""Unittsets for base_model.py"""


import datetime
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test BaseModel class"""
    def test_no_args_instantiates(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_uuid(self):
        """test initialization of class"""
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertIsInstance(bm1, BaseModel)
        self.assertTrue(hasattr(bm1, "id"))
        self.assertNotEqual(bm1.id, bm2.id)
        self.assertIsInstance(bm1.id, str)
        self.assertIsInstance(bm1.created_at, datetime.datetime)
        self.assertIsInstance(bm1.updated_at, datetime.datetime)

        bm1.to_dict()
        self.assertTrue(hasattr(bm1, "__class__"))
        self.assertIsInstance(bm1.created_at, str)
        self.assertIsInstance(bm1.updated_at, str)

    def test_isoformat(self):
        """test isoformat of datettime"""
        now = datetime.datetime(2023, 4, 6, 18, 25, 31, 92221)
        self.assertEqual(now.isoformat(), '2023-04-06T18:25:31.092221')
