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
        key = "{}.{}".format(type(obj), obj['id'])
        # Add object to __objects
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the specified JSON file"""
        with open(FileStorage.__file_path, 'w') as fw:
            json.dump(FileStorage.__objects, fw)

    def reload(self):
        """Deserializes JSON file to __objects"""
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as fr:
                json.load(FileStorage.__objects)
