#!/usr/bin/python3
"""state module contains a subclass of base_model.BaseModel()
"""
from models.base_model import BaseModel


class State(BaseModel):
    """Defines a State class that inherits from BaseModel

        Attributes:
            name (str): name of the state instance
    """
    name = ''
