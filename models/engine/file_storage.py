#!/usr/bin/python3
'''
Class FileStorage that serializes instances to a
JSON file and deserializes JSON file to instances
'''


import json


class FileStorage:
    '''serializes instances to a JSON file and deserializes JSON fileto inst'''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        ''' return __objects dictionary'''
        return FileStorage.__objects

    def new(self, obj):
        '''sets in __objects the obj with key <obj class name>.id'''
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        value_dict = obj
        FileStorage.__objects[key] = value_dict

    def save(self):
        '''serializes __objects to the JSON file (path: __file_path)'''
        objects_dict = {}
        for key, val in FileStorage.__objects.items():
            objects_dict[key] = val.to_dict()

        with open(FileStorage.__file_path, mode='w', encoding="UTF8") as f:
            json.dump(objects_dict, f)

    def reload(self):
        '''Deserializes the JSON file to __objects'''
        from models.base_model import BaseModel

        try:
            with open(FileStorage.__file_path, encoding="UTF8") as f:
                FileStorage.__objects = json.load(f)
            for key, val in FileStorage.__objects.items():
                FileStorage.__objects[key] = BaseModel(**val)
        except FileNotFoundError:
            pass
