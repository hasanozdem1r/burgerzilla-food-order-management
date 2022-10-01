"""
This script is created to prepare api json responses
Hasan Özdemir 02-12-2020
"""
# path : root/customer_ms/customer_application/customer_api/order_utils.py
from flask import jsonify

# Resource : https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.10
def make_response_409() -> jsonify():  # Conflict
    """
    This method is used to return request params related errors. Missing params or misspelling error handled
    :return:
    """
    response_msg: dict = {
        "Server Message": "The request could not be completed due to a conflict with the current state of the resource."
    }
    response = jsonify(response_msg)
    response.status_code = 409
    return response


def make_general_response(message: str) -> jsonify():
    """
    This method is used to make general error messages
    :return: <jsonify>
    """
    response_msg: dict = {"Server Message": message}
    response = jsonify(response_msg)
    response.status_code = 400
    return response


def check_add_customer_params(request_data: dict) -> bool:
    """This method is used to check mandatory fields of model"""
    params = [
        "c-email",
        "c-full-name",
        "c-address",
        "c-city",
        "c-postal-code",
        "c-phone-number",
    ]
    params_check = [item in request_data.keys() for item in params]
    if any(params_check):
        return True
    else:
        return False


def get_add_customer_params(request_data: dict) -> tuple:
    """This method is used to get form data"""
    c_email = request_data["c-email"]
    c_full_name = request_data["c-full-name"]
    c_address = request_data["c-address"]
    c_city = request_data["c-city"]
    c_postal_code = request_data["c-postal-code"]
    c_phone_number = request_data["c-phone-number"]
    return c_email, c_full_name, c_address, c_city, c_postal_code, c_phone_number


def initialize_customer(
    customer, c_email, c_full_name, c_address, c_city, c_postal_code, c_phone_number
):
    """This method is used to initialize customer object"""
    customer.c_email = c_email
    customer.c_full_name = c_full_name
    customer.c_address = c_address
    customer.c_city = c_city
    customer.c_postal_code = c_postal_code
    customer.c_phone_number = c_phone_number
    return customer
