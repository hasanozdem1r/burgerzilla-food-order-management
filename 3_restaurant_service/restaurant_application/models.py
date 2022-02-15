"""
This script is created to create customer model under limitations of ORM approach
Hasan Özdemir 02-09-2022
"""
# path : root/3_restaurant_service/restaurant_application/models.py

# TODO typing implementation
# import from __init__
from . import db

# imports for relationships management
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# base class constructing
Base = declarative_base()


class RestaurantOwnersOrm(db.Model, Base):
    # table name initialization
    __tablename__ = "Restaurant_Owners"  # we can consider as supplier details
    # primary key initialization
    r_o_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # relationship initialization between RestaurantOwnersOrm & RestaurantsOrm (One-to-Many)
    r_o_parent = relationship("RestaurantsOrm", back_populates="r_children")
    # fields initialization continues
    r_o_email = db.Column(db.String(255), nullable=False)
    r_o_full_name = db.Column(db.String(100), nullable=False)
    r_o_address = db.Column(db.String(100), nullable=False)
    r_o_city = db.Column(db.String(25), nullable=False)
    r_o_postal_code = db.Column(db.Integer, nullable=False)
    r_o_phone_number = db.Column(db.String(15), nullable=False)


class RestaurantsOrm(db.Model, Base):
    # table name initialization
    __tablename__ = "Restaurants"
    # primary key initialization
    r_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # relationship initialization between RestaurantsOrm & ProductsOrm (One-to-Many)
    r_parent = relationship("ProductsOrm", back_populates="r_children")
    # foreign key initialization between RestaurantOwnersOrm & RestaurantsOrm (One-to-Many)
    r_o_id = db.Column(
        db.Integer, ForeignKey(column="Restaurant_Owners.r_o_id")
    )  # table_name.column
    r_children = relationship("RestaurantOwnersOrm", back_populates="r_o_parent")
    # fields initialization continues
    r_name = db.Column(db.String(50), nullable=False)
    r_address = db.Column(db.String(100), nullable=False)
    r_city = db.Column(db.String(25), nullable=False)
    r_postal_code = db.Column(db.Integer, nullable=False)
    r_phone_number = db.Column(db.String(15), nullable=False)


class ProductsOrm(db.Model):
    # table name initialization
    __tablename__ = "Products"
    p_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # Foreign key initialization between RestaurantsOrm & ProductsOrm (One-to-Many)
    r_id = db.Column(db.Integer, ForeignKey(column="Restaurants.r_id"))
    # relationship initialization between RestaurantsOrm & ProductsOrm (One-to-Many)
    p_child = relationship("RestaurantsOrm", back_populates="r_parent")
    # fields initialization continues
    p_name = db.Column(db.String(50), nullable=False)
    p_description = db.Column(db.String(255), nullable=False)
    p_image_path = db.Column(db.String(255), nullable=False)
    p_unit_price = db.Column(db.Integer, nullable=False)
