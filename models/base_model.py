#!/usr/bin/python3
"""This module contains the BaseModel class for our Airbnb project"""


import datetime
import uuid


class BaseModel:
    """BaseModel class for our Airbnb project"""
    def __init__(self):
        """BaseModel initialization"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """How BaseModel shoul be printed"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the instance attr updated_at with the current datetime"""
        #return self.updated_at
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """returns a dict containing all keys/values of __dict__
           of the instance
        """
        #self.created_at = self.created_at.isoformat()
        #self.updated_at = self.updated_at.isoformat()

        #self.__dict__["__class__"] = self.__class__.__name__
        #return self.__dict__
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
