#!/usr/bin/python3
"""user module contains a subclass of base_model.BaseModel()
"""
from models.base_model import BaseModel
import models
import hashlib


class User(BaseModel):
    """Defines a class that inherits from BaseModel

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

    def __init__(self, *args, **kwargs):
        classes = {"email": self.email, "first_name": '',
                   "last_name": '', "password": ''}
        super().__init__(**classes)
        super().save()

    def save(self):
        """
        """
        self.password = hash_password(self.password) 
        models.storage.new(self)
        
    def to_dict(self):
        """
        """
        dictionary = super().__dict__.copy()
        dictionary["email"] = User.email
        return dictionary


def hash_password(password):
    # Create the md5 hash object
    md5 = hashlib.md5()
    
    # Update the hash with the password
    md5.update(password.encode())
    
    # Return the hexadecimal representation of the hash
    return md5.hexdigest()
