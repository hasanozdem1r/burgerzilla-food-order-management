"""
This script is created to create customer model under limitations of ORM approach
Hasan Özdemir 02-05-2022
"""
# path : root/customer_ms/customer_application/models.py
# from . import db original
from . import db


class CustomerOrm(db.Model):
    """Customer ORM Model definition"""

    # table name declaration
    __tablename__ = "Customer"
    # table columns declaration
    c_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    c_email = db.Column(db.String(255), nullable=False)
    c_full_name = db.Column(db.String(100), nullable=False)
    c_address = db.Column(db.String(100), nullable=False)
    c_city = db.Column(db.String(25), nullable=False)
    c_postal_code = db.Column(db.Integer, nullable=False)
    c_phone_number = db.Column(db.String(15), nullable=False)

    # creates a full string representation of an object
    def __repr__(self) -> str:
        """
        __repr__ is the special function that returns the string representation of the customer object.
        The goal of __repr__ is to be unambiguous
        :return: <str> representation of customer object
        """
        return f"<Full Name :{self.c_full_name}>"

    def convert_to_json(self) -> dict:
        """
        This method is used to create representable format suitable for JSON based API response
        :return: <dict> JSON based API response
        """
        return {
            "c_email": self.c_email,
            "c_full_name": self.c_full_name,
            "c_address": self.c_address,
            "c_city": self.c_city,
            "c_post_code": self.c_postal_code,
            "c_phone_number": self.c_phone_number,
        }
