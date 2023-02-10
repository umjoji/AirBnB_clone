#!/usr/bin/python3
"""file_storage module contains a storage class for storing class objects
"""
from models.base_model import BaseModel
import json


class FileStorage():
    """Serializes instances to JSON file and deserializes JSON file to instance

    Attributes:
        __file_path (str): path of JSON file in directory
        __objects (dict): stores all created objects with a unique id
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """Appends a newly created object to the __objects dictionary

        Args:
            obj (object): 
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file at __file_path
        """
        with open(self.__file_path, 'w') as f:
            objs = {key: obj.to_dict() for key, obj in self.__objects.items()}
            json.dump(objs, f)

    def reload(self):
        """Deserializes the JSON file at __file_path to __objects
        """
        try:
            with open(self.__file_path, 'r') as f:
                objs = json.load(f)
                for key, value in objs.items():
                    self.__objects[key] = eval(value['__class__'])(**value)
        except FileNotFoundError:
            pass
