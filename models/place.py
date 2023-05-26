#!/usr/bin/python3
"""contains the place class"""


import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """State class"""
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "places"
        city_id = Column(String(60), nullable=False, ForeignKey('cities.id'))
        user_id = Column(String(60), nullable=False, ForeignKey('users.id'))
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float)
        longitude = Column(Float)
        amenity_ids = []
    else:
        city_id = ""
	user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
	max_guest = 0
	price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []
