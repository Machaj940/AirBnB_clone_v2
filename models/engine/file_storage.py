#!/usr/bin/python3
'''
Write a class FileStorage that serializes instances to a
JSON file and deserializes JSON file to instances
'''
import json
import models


class FileStorage:
    '''serializes instances to a JSON file and deserializes JSON file
    to instances'''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        ''' return __objects dictionary'''
        return self.__objects

    def new(self, obj):
        '''sets in __objects the obj with key <obj class name>.id'''
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        value_dict = obj.to_dict
        FileStorage.__objects[key] = value_dict

    def save(self):
        '''serializes __objects to the JSON file (path: __file_path)'''
        with open(FileStorage.__file_path, mode='w', encoding="utf-6") as f:
            json.dump(FileStorage.__objects, f, indent=4)

    def reload(self):
        '''Deserializes the JSON file to __objects'''
        try:
            with open(FileStorage.__file_path, encoding="utf-8") as f:
                FileStorage.__objects = json.load(f)
        except FileNotFoundError:
            pass
