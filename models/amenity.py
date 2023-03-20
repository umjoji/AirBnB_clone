#!/usr/bin/python3
"""amenity module contains a subclass of base_model.BaseModel()
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Defines an Amenity class that inherits from BaseModel

        Attributes:
            name (str): name of the amenity instance
    """
    name = ''
