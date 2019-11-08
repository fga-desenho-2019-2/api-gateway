from flask import Flask, jsonify, Blueprint, request
from flask_cors import CORS
import requests
import os

orders_blueprint = Blueprint('orders', __name__)
CORS(orders_blueprint)

@orders_blueprint.route('/api/order-bag', methods=['POST'])
def order_bag():
    data = request.get_json()

    # request pra checar pagamento
    # response_payment = requests.post()
    response_payment = 200

    # if response_payment.status_code == 200:
    if response_payment == 200:
        response_order = requests.post('%s/create_order/' % os.getenv('ORDERS_PATH'), json=data) 
    
        return jsonify(response_order.json()), response_order.status_code
    else:
        return 400