#!/usr/bin/python
""" Module that contains the Basemodel for the project"""
import models
import uuid
from datetime import datetime


class BaseModel:
    """ Base Model Class """

    def __init__(self, *args, **kwargs):
        """
        Initialization methon to initilize each instance of BaseModel
        Args:
            self: Refers to the Object created.
        Attributes:
            id: Unique Identification number for each instance
            created_at: Time the each instance was created
            updated_at: Last time the instance was updated
        """
        if len(kwargs):
            iso_date = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    self.__dict__[key] = datetime.strptime(value, iso_date)
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            models.storage.new(self)

    def save(self):
        """ Updates instance attribute *updated_at* with current datetime """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """ Returns a dictionary of the instance attributes"""
        base_dict = self.__dict__.copy()
        base_dict["created_at"] = self.created_at.isoformat()
        base_dict["updated_at"] = self.updated_at.isoformat()
        base_dict["__class__"] = self.__class__.__name__

        return base_dict

    def __str__(self):
        """ String Representation of base model"""
        return "[{}] ({}) {} ".format(self.__class__.__name__,
                                      self.id, self.__dict__)
