#!/usr/bin/python3
"""
Class City
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    The city of service
    Attributes:
        state_id: string - empty string: it will be the State.id
        name: string - empty string
    """
    name = ""
    state_id = ""
