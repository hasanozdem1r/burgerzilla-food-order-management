"""
This script is created to prepare api json responses
Hasan Özdemir 02-12-2020
"""
# path : root/1_customer_service/customer_application/customer_api/order_utils.py
from flask import jsonify

# Resource : https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.10

# HTTP MESSAGES

def make_response_409() -> jsonify():  # Conflict
    """This method is used to return request params related errors. Missing params or misspelling error handled"""
    response_msg: dict = {
        "Server Message": "The request could not be completed due to a conflict with the current state of the resource."}
    response = jsonify(response_msg)
    response.status_code = 409
    return response


def make_general_response(message: str) -> jsonify():
    """This method is used to make general error messages"""
    response_msg: dict = {"Server Message": message}
    response = jsonify(response_msg)
    response.status_code = 400
    return response

# ENDPOINT HELPERS

def check_add_order_keys(request_data:dict)->bool:
    """This method is used to check mandatory fields of model"""
    params = ['o-id', 'c-id', 'o-address', 'o-city', 'o-postal-code', 'o-status', 'o-date']
    params_check = [item in request_data.keys() for item in params]
    if any(params_check):
        return True
    else:
        return False

def get_add_order_params(request_data:dict):
    """This method is used to get form data"""
    o_id=request_data['o-id']
    c_id = request_data['c-id']
    o_address = request_data['o-address']
    o_city = request_data['o-city']
    o_postal_code = request_data['o-postal-code']
    o_status = request_data['o-status']
    o_date = request_data['o-date']
    o_phone_number=request_data['o-phone-number']
    order_details=dict()
    for i in range(len(o_id)):
        order_details['o-id']=request_data["o-id"][i]['o-d-id']
        order_details['o-id'] = request_data["o-id"][i]['o-id']
        order_details['p-id'] = request_data["o-id"][i]['p-id']
        order_details['o-quantity'] = request_data["o-id"][i]['o-quantity']
        order_details['order-price'] = request_data["o-id"][i]['order-price']
    return o_id,c_id, o_address,o_city,o_postal_code,o_phone_number,o_status,o_date,order_details

# ORM HELPERS

def initialize_order(order,o_id,c_id, o_address,o_city,o_postal_code,o_phone_number,o_status,o_date):
    """This method is used to initialize order object"""
    order.o_id = o_id
    order.c_id = c_id
    order.o_address = o_address
    order.o_city=o_city
    order.o_postal_code = o_postal_code
    order.o_phone_number=o_phone_number
    order.o_status = order.o_status
    order.o_date = o_date
    return order