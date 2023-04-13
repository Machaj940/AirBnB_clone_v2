#!/usr/bin/python3
"""This module contains the BaseModel class for our Airbnb project"""


import datetime
import uuid
from models import storage


class BaseModel:
    """BaseModel class for our Airbnb project"""
    def __init__(self, *args, **kwargs):
        """BaseModel initialization with args and kwargs"""
        if (len(kwargs) == 0):
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)
        else:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.datetime.strptime(
			kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
		else:
                    self.__dict__[key] = kwargs[key]

    def __str__(self):
        """How BaseModel shoul be printed"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the instance attr updated_at with the current datetime"""
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dict containing all keys/values of __dict__
           of the instance
        """
        cp_dct = dict(self.__dict__)
        cp_dct["__class__"] = self.__class__.__name__
        cp_dct["updated_at"] = self.updated_at.isoformat()
        cp_dct["created_at"] = self.created_at.isoformat()
        return cp_dct

# self.__class__.__name__ is equivalent to type(self).__name__
