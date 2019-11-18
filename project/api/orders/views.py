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


@orders_blueprint.route('/api/list-user-orders/<string:cpf>/<int:status>', methods=['GET'])
def user_orders(cpf, status):
    response = requests.get("%s/api/list_user_orders/%s/%s" % (os.getenv('ORDERS_PATH'), cpf, status))
    return jsonify(response.json()), response.status_code


@orders_blueprint.route('/api/list-restaurant-orders/<string:cnpj>/<int:status>', methods=['GET'])
def restaurant_orders(cnpj, status):
    response = requests.get("%s/api/list_restaurant_orders/%s/%s" % (os.getenv('ORDERS_PATH'), cnpj, status))
    return jsonify(response.json()), response.status_code


@orders_blueprint.route('/api/update-status-order/<int:id>/<int:status>', methods=['PUT'])
def update_status_order(id, status):
    response = requests.put("%s/api/update_status_order/%s/%s" % (os.getenv('ORDERS_PATH'), id, status))
    return jsonify(response.json()), response.status_code