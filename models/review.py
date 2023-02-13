#!/usr/bin/python3
"""review module contains a subclass of base_model.BaseModel()
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Defines a Review class that inherits from BaseModel
    
        Attributes:
            place_id (str): unique identifier of the review's place
            user_id (str): unique identifier of the review owner
            text (str): text body of the review
    """
    place_id = ''
    user_id = ''
    text = ''
