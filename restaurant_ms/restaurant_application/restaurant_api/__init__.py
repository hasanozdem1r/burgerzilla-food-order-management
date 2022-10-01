"""
This script is used to create blueprint object for restaurant api
Hasan Özdemir 02-05-2022
"""
# path :  root/restaurant_ms/restaurant_application/restaurant_api/__init.py
from flask import Blueprint

# create the blueprint object
r_api_blueprint = Blueprint("restaurant_api", __name__)
#  import the routes.py
from . import routes
