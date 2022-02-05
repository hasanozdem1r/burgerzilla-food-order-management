"""
This script is created to create customer model under limitations of ORM approach
Hasan Özdemir 02-05-2022
"""
# path : root/1_customer_service/customer_application/models.py

# TODO typing implementation
from . import db
from datetime import datetime

class Customer(db.Model):
    """
    Customer Model
    """
    # please look at 3_project_docs/burgerzilla_db_schema.md docs to understand Customer Model
    __tablename__='Customer'
    c_id=db.Column(db.Integer, primary_key=True,autoincrement=True)
    c_email=db.Column(db.String(255), nullable=False)
    c_full_name=db.Column(db.String(100),nullable=False)
    c_address = db.Column(db.String(100), nullable=False)
    c_city = db.Column(db.String(25), nullable=False)
    c_post_code = db.Column(db.Integer, nullable=False)
    c_phone_number = db.Column(db.String(15), nullable=False)

    def __repr__(self)->str:
        """
        __repr__ is the special function that returns the string representation of the customer object.
        :return: <str> representation of customer object
        """
        return f'<Full Name :{self.c_full_name}>'

    def convert_to_json(self)->dict:
        """
        This method is used to create representable format suitable for JSON based API response
        :return: <dict> JSON based API response
        """
        return {
            'c_email' : self.c_email,
            'c_full_name':self.c_full_name,
            'c_address':self.c_address,
            'c_city':self.c_city,
            'c_post_code':self.c_post_code,
            'c_phone_number':self.c_phone_number
        }