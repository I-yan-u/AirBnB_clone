#!usr/bin/python3
"""Definition of the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage:
    """
    Class File Storage, Handles user data storage
    Attributes:
        __file_path: location and name of file.
        __objects: holds dict format of Basemodel instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns all objects in file storage"""
        return FileStorage.__objects

    def new(self, obj):
        """
        Appends new objects into the filestorage
        Arg:
            obj (BaseModel): BaseModel objects.
        """
        FileStorage.__objects["{}.{}".format(obj.__class__.__name__,
                                              obj.id)] = obj

    def save(self):
        """ Save content of __objects to file storage"""
        obj_cpy = FileStorage.__objects
        obj_dict = {
            obj: obj_cpy[obj].to_dict() for obj in obj_cpy.keys()
        }
        with open(FileStorage.__file_path, "w") as file:
            file.write(json.dumps(obj_dict))

    def reload(self):
        """ reload objects from file storage"""
        try:
            with open(FileStorage.__file_path, "r") as f:
                objects_dict = json.load(f)
                for obj in objects_dict.values():
                    class_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(class_name)(**obj))
        except IOError:
            pass
