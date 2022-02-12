"""
This script is used to define customer_api endpoints
Hasan Özdemir 02-05-2022
"""
# path : root/1_customer_service/customer_application/customer_api/routes.py
# API ROOT :  http://0.0.0.0:5001/burgerzilla-customer/1.0.0/
from . import o_api_blueprint
from .. import db, login_manager
from ..models import OrdersOrm,OrderDetailsOrm
from flask import make_response, jsonify, request, json
from flask_login import current_user, login_user, logout_user, login_required
from passlib.hash import sha256_crypt

API_ROOT: str = "/burgerzilla-order/1.0.0"

# GET : localhost:5002/burgerzilla-order/1.0.0/orders
@o_api_blueprint.route(f'{API_ROOT}/orders', methods=['GET'])
def get_all_orders() -> json:
    """
    This endpoint is used to retrieve all orders with no filtering
    :return: <flask.json> return all orders
    """
    # create empty order list
    orders = []
    # loop through all Customer
    for row in OrdersOrm.query.all():
        # append to order list
        orders.append(row.convert_to_json())

    # create presentable format suitable for JSON
    response = jsonify(orders)
    # return all customers
    return response

