#!/usr/bin/python3
"""user module contains a subclass of base_model.BaseModel()
"""
from models.base_model import BaseModel


class User(BaseModel):
    """Defines a User class that inherits from BaseModel

        Attributes:
            email (str): user's email
            first_name (str): user's first name
            last_name (str): user's last name
            password (str): user's password
    """
    email = ''
    first_name = ''
    last_name = ''
    password = ''

