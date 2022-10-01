"""
This script is used to define customer_api endpoints
Hasan Özdemir 02-13-2022
"""
# path : root/order_ms/order_application/order_api/routes.py
import datetime

from . import o_api_blueprint
from .. import db
from ..models import OrdersOrm, OrderDetailsOrm
from flask import jsonify, request, json
from .order_utils import (
    make_response_409,
    make_general_response,
    check_add_order_keys,
    get_add_order_params,
    initialize_order,
)
from json import loads

API_ROOT: str = "/burgerzilla-order/1.0.0"


# GET FORMAT: localhost:5002/burgerzilla-order/1.0.0/orders?customer-id=?
# GET EXAMPLE : localhost:5002/burgerzilla-order/1.0.0/orders?customer-id=2
# GET FORMAT: localhost:5002/burgerzilla-order/1.0.0/orders?restaurant-id=?
# GET EXAMPLE : localhost:5002/burgerzilla-order/1.0.0/orders?restaurant-id=2
@o_api_blueprint.route(f"{API_ROOT}/orders", methods=["GET"])
def get_all_orders_based_on_customer():
    """
    This endpoint is used to retrieve all orders based on customer-id
    :return: <flask.json> return all orders
    """
    try:
        if request.method == "GET":
            if "customer-id" in request.args:
                customer_id = request.args.get("customer-id")
                customer_orders = OrdersOrm.query.filter_by(c_id=customer_id)
                c_orders = []
                for order in customer_orders:
                    c_orders.append(order)
                response = jsonify(c_orders)
                return response
            else:
                # return information message
                make_response_409()
    except Exception as general_error:  # disadvantage of here is being so broad. It may occur some performance issue
        # return information message
        make_general_response(message=str(general_error))


# GET FORMAT : localhost:5002/burgerzilla-order/1.0.0/order?customer-id&order-id
# GET EXAMPLE : localhost:5002/burgerzilla-order/1.0.0/order?customer-id=1&order-id=1
@o_api_blueprint.route(f"{API_ROOT}/order", methods=["GET"])
def get_order_based_on_customer_and_order():
    """
    This endpoint is used to retrieve order based on customer-id and order-id
    :return: <flask.json> return all orders
    """
    try:
        if request.method == "GET":
            if "customer-id" in request.args and "order-id" in request.args:
                customer_id = request.args.get("customer-id")
                order_id = request.args.get("order-id")
                customer_orders = OrdersOrm.query.filter_by(
                    c_id=customer_id, o_id=order_id
                )
                c_orders = [order for order in customer_orders]
                response = jsonify(c_orders)
                return response
            else:
                # return information message
                make_response_409()
    except Exception as general_error:  # disadvantage of here is being so broad. It may occur some performance issue
        # return information message
        make_general_response(str(general_error))


# POST : http://0.0.0.0:5001/burgerzilla-order/1.0.0/order
@o_api_blueprint.route(f"{API_ROOT}/order", methods=["POST"])
def create_new_order() -> json:
    """
    This method is used to create customer with given API endpoint
    :return: <flask.json> information message
    """
    if request.method == "POST":
        try:
            form_data = request.get_json()
            is_params_valid = check_add_order_keys(request_data=form_data)
            if is_params_valid:
                # get form data
                (
                    o_id,
                    c_id,
                    o_address,
                    o_city,
                    o_postal_code,
                    o_phone_number,
                    o_status,
                    o_date,
                    order_details,
                ) = get_add_order_params(request_data=form_data)
                # initialize order
                order = OrdersOrm()
                # fill order object
                order = initialize_order(
                    order,
                    form_data["o-id"][0]["o-id"],
                    c_id,
                    o_address,
                    o_city,
                    o_postal_code,
                    o_phone_number,
                    o_status,
                    o_date,
                )
                # add to session
                db.session.add(order)
                # apply changes
                db.session.commit()
                # create information message which is presentable format suitable for JSON
                response = jsonify({"Message": "Order have added"})
                # return information message
                return response
            else:
                response = make_response_409()
                return response
        except Exception as error:
            response = make_general_response(str(error))
            return response
