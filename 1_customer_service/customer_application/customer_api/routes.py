"""
This script is used to define customer_api endpoints
Hasan Özdemir 02-05-2022
"""
# path : root/1_customer_service/customer_application/customer_api/routes.py
# API ROOT :  http://0.0.0.0:5001/burgerzilla-customer/1.0.0/
from . import c_api_blueprint
from .. import db
from ..models import Customer
from flask import jsonify, request, json
from .customer_utils import make_response_409,make_general_response
from requests import get

CUSTOMER_API_ROOT: str = "/burgerzilla-customer/1.0.0"
ORDER_API_ROOT:str = "http://localhost:5002/burgerzilla-order/1.0.0"


# GET : http://0.0.0.0:5001/burgerzilla/v1/customers
@c_api_blueprint.route(f'{CUSTOMER_API_ROOT}/customers', methods=['GET'])
def get_all_customers() -> json:
    """
    This endpoint is used to retrieve all customers
    :return: <flask.json> return all customers
    """
    # create empty customer list
    customers = []
    # loop through all Customer
    for row in Customer.query.all():
        # append to customer list
        customers.append(row.convert_to_json())

    # create presentable format suitable for JSON
    response = jsonify(customers)
    # return all customers
    return response


# POST : http://0.0.0.0:5001/burgerzilla/v1/customers
@c_api_blueprint.route('/burgerzilla/v1/customers', methods=['POST'])
def create_new_customer() -> json:
    """
    This method is used to create customer with given API endpoint
    :return: <flask.json> information message
    """
    # get form-data
    c_email = request.form['c-email']
    c_full_name = request.form['c-full-name']
    c_address = request.form['c-address']
    c_city = request.form['c-city']
    c_post_code = request.form['c-post-code']
    c_phone_number = request.form['c-phone-number']
    # initialize Customer
    customer = Customer()
    # add data which is received from api user
    customer.c_email = c_email
    customer.c_full_name = c_full_name
    customer.c_address = c_address
    customer.c_city = c_city
    customer.c_post_code = c_post_code
    customer.c_phone_number = c_phone_number
    # add customer
    db.session.add(customer)
    # apply changes
    db.session.commit()
    # create information message which is presentable format suitable for JSON
    response = jsonify({'message': 'Customer have added', 'customer information': customer.convert_to_json()})
    # return information message
    return response


# GET : http://0.0.0.0:5001/burgerzilla-customer/1.0.0/orders?customer-id=1
@c_api_blueprint.route(f'{CUSTOMER_API_ROOT}/orders', methods=['GET'])
def get_all_orders_based_on_customer() -> json:
    """
    This endpoint is used to retrieve all orders based on customer-id
    :return: <flask.json> return all customer's orders
    """
    try:
        if "customer-id" in request.args:
            customer_id = request.args.get('customer-id')
            query_str:str = f"{ORDER_API_ROOT}/orders?customer-id={customer_id}"
            response:dict = get(query_str).json()
            return jsonify(response)
        else:
            # return information message
            make_response_409()
    except Exception as general_error: # disadvantage of here is being so broad. It may occur some performance issue
        # return information message
        make_general_response(str(general_error))