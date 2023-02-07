#!/usr/bin/python3
"""

"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """ Base model for AirBnB package"""

    def __init__(self):
        """ 
        Initialization methon to initilize each instance of BaseModel
        Args:
            self: Refers to the Object created.
        Attributes:
            id: Unique Identification number for each instance
            created_at: Time the each instance was created
            updated_at: Last time the instance was updated
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def save(self):
        """ Updates instance attribute *updated_at* with current datetime """
        self.updated_at = datetime.today()

    def to_dict(self):
        """ Returns a dictionary of the instance attributes"""
        base_dict = self.__dict__.copy()
        base_dict["created_at"] = self.created_at.isoformat()
        base_dict["updated_at"] = self.updated_at.isoformat()
        base_dict["__class__"] = self.__class__.__name__

        return base_dict

    def __str__(self):
        """ String Representation of base model"""
        return "[{}] ({}) {}".format(self.__class__.__name__, \
                self.id, self.__dict__)
