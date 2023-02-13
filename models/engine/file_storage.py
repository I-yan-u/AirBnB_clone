#!/usr/bin/python3
"""
File Storage module
"""
import json
import models
import os.path


class FileStorage:
    """
    Purpose:
    serializes and deserializes class objects to and from JSON file

    Args:
    __objects: contains objects imported for serialization
    __file_path: The path of the JSON file
    """
    __file_path = "objects.json"
    __objects = {}

    def all(self):
        """Returns __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets __objects with obj parameter"""
        # define key
        key = "{}.{}".format(type(obj), obj.id)
        # Add object to __objects
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the specified JSON file"""
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as fw:
            d = {k : v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, fw)

    def reload(self):
        """Deserializes JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as fr:
               ob_dict = json.load(fr)
               for o in ob_dict.values():
                   cls_name = o['__class__']
                   del o['__class__']
                   FileStorage.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
