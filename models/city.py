#!/usr/bin/python3
"""city module contains a subclass of base_model.BaseModel()
"""
from models.base_model import BaseModel


class City(BaseModel):
    """Defines a City class that inherits from BaseModel
    
        Attributes:
            name (str): name of the city instance
            state_id (str): unique identifier of the city's home state
    """
    name = ''
    state_id = ''
