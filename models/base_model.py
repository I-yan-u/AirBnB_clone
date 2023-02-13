#!/usr/bin/python
""" Module that contains the Basemodel for the project"""
import uuid
from datetime import datetime


class BaseModel:
    """ Base Model Class """

    def __init__(self):
        """ Initializes all instance attributes """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ Print the representation of the object """
        return f"[{__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the updated_at instance variable"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Returns a copy of __dict__"""
        rdict = self.__dict__.copy()
        rdict['created_at'] = self.created_at.isoformat()
        rdict['updated_at'] = self.updated_at.isoformat()
        rdict['__class__'] = __class__.__name__
        return rdict
