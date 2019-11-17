from flask import Flask, jsonify, Blueprint, request
from flask_cors import CORS
import requests
import os

restaurant_blueprint = Blueprint('restaurant', __name__)
CORS(restaurant_blueprint)

@restaurant_blueprint.route('/api/restaurants', methods=['GET'])
def get_all_restaurant():
    response = requests.get('%s/api/restaurant' % os.getenv('RESTAURANT_PATH')) 

    if response.status_code == 200:
        return jsonify(response.json()), response.status_code

    return 400

@restaurant_blueprint.route('/api/restaurant/<int:pk>', methods=['GET'])
def get_one_restaurant():
    response = requests.get('%s/api/restaurant/<int:pk>' % os.getenv('RESTAURANT_PATH')) 
    
    if response.status_code == 200:
        return jsonify(response.json()), response.status_code

    return 400

@restaurant_blueprint.route('/api/items', methods=['GET'])
def get_all_items():
    response = requests.get('%s/api/item' % os.getenv('RESTAURANT_PATH')) 
    
    if response.status_code == 200:
        return jsonify(response.json()), response.status_code

    return 400

@restaurant_blueprint.route('/api/item/<int:pk>', methods=['GET'])
def get_one_item():
    response_item = requests.get('%s/api/item/<int:pk>' % os.getenv('RESTAURANT_PATH')) 
    
    if response.status_code == 200:
        return jsonify(response.json()), response.status_code

    return 400
