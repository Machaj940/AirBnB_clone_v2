#!/usr/bin/python3
'''class BaseModel defines all common attributes/methods for other classes'''


import uuid
from datetime import datetime

class BaseModel:
    '''defines all common attributes/methods for other classes'''
    def __init__(self):
        '''initializes public instance attributes'''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        '''Return string represtentation of basemodel'''
        return "[" + type(self).__name__ + "]" "(" + self.id + ")" + str(self.__dict__)
    # or return "return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        '''updates the public instance attribute updated_at with the current datetime'''
        return self.updated_at

    def to_dict(self):
        '''returns a dictionary containing all keys/values of __dict__ of the instance'''
        cp_dct = dict(self.__dict__)
        cp_dct['__class__'] = self.__class__.__name__
        cp_dct['updated_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        cp_dct['created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")

        return (cp_dct)
