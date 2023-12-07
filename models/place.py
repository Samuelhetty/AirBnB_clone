#!/usr/bin/python3
"""
Place Class from Models Module
"""
import os
from models.base_model import BaseModel, Base


class Place(BaseModel, Base):
    """Place class handles all application places"""
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
    review_ids = []
