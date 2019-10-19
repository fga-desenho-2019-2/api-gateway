from flask import Flask, jsonify, Blueprint, request
from flask_cors import CORS
import requests
import os

orders_blueprint = Blueprint('orders', __name__)
CORS(orders_blueprint)

@orders_blueprint.route('/api/order', methods=['GET'])
def get_order():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })