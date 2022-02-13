"""
This script is created to prepare api json responses
Hasan Özdemir 02-12-2020
"""
# path : root/1_customer_service/customer_application/customer_api/order_utils.py
from flask import jsonify

# Resource : https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.10
def make_response_409()->jsonify(): # Conflict
    """
    This method is used to return request params related errors. Missing params or misspelling error handled
    :return:
    """
    response_msg:dict={"Server Message":"The request could not be completed due to a conflict with the current state of the resource."}
    response = jsonify(response_msg)
    response.status_code = 409
    return response

def make_general_response(message:str)->jsonify():
    """
    This method is used to make general error messages
    :return: <jsonify>
    """
    response_msg:dict={"Server Message":message}
    response = jsonify(response_msg)
    response.status_code = 400
    return response