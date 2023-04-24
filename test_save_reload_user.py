#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new User --")
my_user = User()
my_user.first_name = "Betty"
my_user.last_name = "Bar"
my_user.email = "airbnb@mail.com"
my_user.password = "root"
my_user.save()
print(my_user)

print("-- Create a new User 2 --")
my_user2 = User()
my_user2.first_name = "John"
my_user2.email = "airbnb2@mail.com"
my_user2.password = "root"
my_user2.save()
print(my_user2)

print("-- Create a State --")
my_state = State()
my_state.name = "California"
my_state.save()
print(my_state)

print("-- Create a City --")
my_city = City()
my_city.name = "Los Angeles"
my_city.save()
print(my_city)

print("-- Create a Amenity --")
my_amenity = Amenity()
my_amenity.name = "Wi-fi"
my_amenity.save()
print(my_amenity)

print("-- Create a Place --")
my_place = Place()
my_place.name = "Casa Keja"
my_place.price_by_night = 500
my_place.save()
print(my_place)

print("-- Create a review --")
my_review = Review()
my_review.text = "Very comfortable"
my_review.save()
print(my_review)
