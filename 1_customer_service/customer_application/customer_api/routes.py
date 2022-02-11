"""
This script is used to define customer_api endpoints
Hasan Özdemir 02-05-2022
"""
# path : root/1_customer_service/customer_application/customer_api/routes.py
# API ROOT :  http://0.0.0.0:5001/burgerzilla-customer/1.0.0/
from . import c_api_blueprint
from .. import db, login_manager
from ..models import Customer
from flask import make_response, jsonify, request, json
from flask_login import current_user, login_user, logout_user, login_required
from passlib.hash import sha256_crypt

API_ROOT: str = "/burgerzilla-customer/1.0.0"


@login_manager.user_loader
def load_customer(c_id: int) -> Customer:
    """
    This callback is used to reload the user object from the user ID stored in the session
    :param c_id: <int> customer id
    :return: <Customer> return Customer object
    """
    return Customer.filter_by(c_id=c_id)


# GET : http://0.0.0.0:5001/burgerzilla/v1/customers
@c_api_blueprint.route(f'{API_ROOT}/customers', methods=['GET'])
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
