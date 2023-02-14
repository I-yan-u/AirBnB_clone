#!/usr/bin/python3
"""
Class Review
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    The Review of the serices
    Attribute:
        place_id: string - empty string: it will be the Place.id
        user_id: string - empty string: it will be the User.id
        text: string - empty string
    """
    place_id = ""
    user_id = ""
    text = ""
