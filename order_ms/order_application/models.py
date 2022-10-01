"""
This script is created to create order model under limitations of ORM approach
Hasan Özdemir 02-09-2022
"""
# path : root/order_ms/order_application/models.py

# from __init__ import db
from . import db

# imports for relationships management
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, Enum

# column type related libraries
from datetime import datetime
import enum

# base class constructing
Base = declarative_base()


class OrderStatus(enum.Enum):
    """
    FOR ALL LIST CHECK THE LINK , FOR NOW OUT OF SCOPE
    https://support.bigcommerce.com/s/article/Order-Statuses
    """

    OK = "ACCEPTED"  # selection and payment successfully done
    ONGOING = "AWAITING"  # order is preparing
    R_FAIL = "R-CANCELLED"  # restaurant is cancelled
    C_FAIL = "C-CANCELLED"  # customer is cancelled
    FINISH = "COMPLETED"  # order completed


class OrdersOrm(db.Model, Base):
    # table name initialization
    __tablename__ = "orders"
    # primary key initialization
    o_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # relationship initialization between OrdersOrm & OrderDetailsOrm (One-to-Many)
    o_parent = relationship(
        "OrderDetailsOrm", uselist=False, back_populates="o_d_children"
    )
    # fields initialization continues
    c_id = db.Column(db.Integer, nullable=False)
    o_address = db.Column(db.String(100), nullable=False)
    o_city = db.Column(db.String(25), nullable=False)
    o_postal_code = db.Column(db.Integer, nullable=True)
    o_phone_number = db.Column(db.String(15), nullable=False)
    o_status = db.Column(Enum(OrderStatus), default=OrderStatus.OK)
    o_date = db.Column(db.Date, nullable=False, default=datetime.utcnow)


class OrderDetailsOrm(db.Model, Base):
    # table name initialization
    __tablename__ = "order_details"
    # primary key initialization
    o_d_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # relationship initialization between OrdersOrm & OrderDetailsOrm (One-to-Many)
    o_d_children = relationship("OrdersOrm", uselist=False, back_populates="o_parent")
    # foreign key initialization between OrdersOrm & OrderDetailsOrm (One-to-Many)
    o_id = db.Column(db.Integer, ForeignKey(column="orders.o_id"), nullable=False)
    # fields initialization continues
    p_id = db.Column(db.Integer, nullable=False)
    order_quantity = db.Column(db.Integer, nullable=False)
    order_price = db.Column(db.Integer, nullable=False)
