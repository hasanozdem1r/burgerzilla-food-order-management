"""
This script is used to define customer_api endpoints
Hasan Özdemir 02-05-2022
"""
# path : root/1_customer_service/customer_application/customer_api/routes.py
# API ROOT :  http://0.0.0.0:5001/burgerzilla-customer/1.0.0/
from . import c_api_blueprint
from .. import db
from ..models import CustomerOrm
from flask import jsonify, request, json
from .customer_utils import make_response_409,make_general_response,check_add_customer_params,get_add_customer_params,initialize_customer
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


# POST : http://0.0.0.0:5001/burgerzilla/v1/customer
@c_api_blueprint.route('/burgerzilla/v1/customer', methods=['POST'])
def create_new_customer() -> json:
    """
    This method is used to create customer with given API endpoint
    :return: <flask.json> information message
    """
    if request.method=='POST':
        try:
            form_data=request.get_json()
            is_params_valid=check_add_customer_params(request_data=form_data)
            if is_params_valid:
                # get form data
                c_email,c_full_name,c_address,c_city,c_postal_code,c_phone_number=get_add_customer_params(request_data=form_data)
                # initialize order
                customer=CustomerOrm()
                # fill order object
                customer=initialize_customer(customer,c_email,c_full_name,c_address,c_city,c_postal_code,c_phone_number)
                # add to session
                db.session.add(customer)
                # apply changes
                db.session.commit()
                # create information message which is presentable format suitable for JSON
                response = jsonify({'Message': 'Customer have added'})
                # return information message
                return response
            else:
                response = make_response_409()
                return response
        except Exception as general_error:
            response=make_general_response(str(general_error))
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