"""
This script is used to create blueprint object for customer api
Hasan Özdemir 02-05-2022
"""
# path :  root/1_customer_service/customer_application/customer_api/__init.py
from flask import Blueprint

# create the blueprint object
o_api_blueprint = Blueprint("customer_api", __name__)
#  import the routes.py
from . import routes
