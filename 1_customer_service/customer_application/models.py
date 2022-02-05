
from . import db
from datetime import datetime

class Customer(db.Model):
    __tablename__='Customer'
    c_id=db.Column(db.Integer, primary_key=True)
    c_email=db.Column(db.String(255), nullable=False)
    c_full_name=db.Column(db.String(100),nullable=False)
    c_address = db.Column(db.String(100), nullable=False)
    c_city = db.Column(db.String(25), nullable=False)
    c_post_code = db.Column(db.Integer, nullable=False)
    c_phone_number = db.Column(db.String(15), nullable=False) #


class Orders(db.Model):
    __tablename__ = 'Orders'
    o_id=db.Column(db.Integer, primary_key=True)
    c_id=db.Column(db.Integer,db.ForeignKey('Customer.c_id'),nullable=False)
    o_address=db.Column(db.String(250),nullable=False)
    o_city=db.Column(db.String(25),nullable=False)
    o_postal_code=db.Column(db.Integer, nullable=False)
    o_phone_number=db.Column(db.String(15), nullable=False)
    o_status=db.Column(db.String(25),nullable=False)
    o_date=db.Column(db.DateTime, default=datetime.utcnow)

