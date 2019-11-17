from flask import Flask, jsonify, Blueprint, request
from flask_cors import CORS
import requests
import os

orders_blueprint = Blueprint('orders', __name__)
CORS(orders_blueprint)

@orders_blueprint.route('/api/order-bag', methods=['POST'])
def order_bag():
    data = request.get_json()

    response_order = requests.post('%s/api/create_order/' % os.getenv('ORDERS_PATH'), json=data) 

    if response_order.status_code == 201:
        return jsonify(response_order.json()), response_order.status_code

    return 400