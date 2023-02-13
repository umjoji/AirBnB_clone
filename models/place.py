#!/usr/bin/python3
"""place module contains a subclass of base_model.BaseModel()
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Defines a Place class that inherits from BaseModel

        Attributes:
            city_id (str): unique identifier of the place's city
            user_id (str): unique identifier of the user
            name (str): name of the place for lease
            description (str): description of the place
            number_rooms (int): number of rooms in place
            number_bathrooms (int): number of bathrooms in place
            max_guest (int): maximum number of guests allowed
            price_by_night (int): price to lease place per night
            latitude (float): location of place on horizontal plane to equator
            longitude (float): location of place vertical to prime meridian
            amenity_ids (list): list of unique identifiers of place's amenities
    """
    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
