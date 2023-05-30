#!/usr/bin/python3
"""contains the place class"""


import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.sql.schema import Table
from sqlalchemy.orm import relationship


if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    metadata = Base.metadata
    place_amenity = Table('place_amenity', metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id'), primary_key=True,
                                 nullable=False),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id'), primary_key=True,
                                 nullable=False)
                          )


class Place(BaseModel, Base):
    """State class"""
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "places"
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float)
        longitude = Column(Float)
        amenity_ids = []
        reviews = relationship("Review", backref="place", cascade="delete")
        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False, backref='place_amenities')
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

        @property
        def reviews(self):
            review_dict = models.storage.all(Review)
            place_query = self.id
            review_list = []
            for k, v in review_dict.items():
                if v.place_id == self.id:
                    review_list.append(v)
            return review_list

        @property
        def amenities(self):
            '''
                 Returns a list containing the amenities ids
            '''
            return self.amenity_ids

        @amenities.setter
        def amenities(self, obj=None):
            '''
                Sets the amenities ids to a list
            '''
            self.amenity_ids = obj.id
            if obj.__class__.__name__ != "Amenity":
                return
            amenity_dict = models.storage.all(obj)
            place_id = self.id
            for key, val in amenity_dict.items():
                if self.id == val.place_id:
                    self.amenity_ids.append(val.id)
