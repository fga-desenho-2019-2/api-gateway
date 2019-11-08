from flask import Flask, jsonify, Blueprint, request
from flask_cors import CORS
import requests
import os

orders_blueprint = Blueprint('orders', __name__)
CORS(orders_blueprint)

@orders_blueprint.route('/api/order-bag', methods=['POST'])
def order_bag():
    data = request.get_json()

    # items = data.pop('items')

    # # print(data)
    # print(data)
    response = requests.post('%s/create_order/' % os.getenv('ORDERS_PATH'), json=data)    
    # response = request.post('http://0.0.0.0:8002/create_item/' % os.getenv('ORDERS_PATH'), json=items)

    return jsonify(response.json()), response.status_code