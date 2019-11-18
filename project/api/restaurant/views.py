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

    return response.status_code

@restaurant_blueprint.route('/api/restaurant/<str:pk>', methods=['GET'])
def get_one_restaurant(pk):
    response = requests.get(f'%s/api/restaurant/{pk}' % os.getenv('RESTAURANT_PATH')) 
    data = response.json()
    
    if data['image']:
        data['image'] = f"http://restaurant.marques.rocks/api/restaurant-image/{pk}"
    
    if response.status_code == 200:
        return jsonify(data), response.status_code

    return response.status_code

@restaurant_blueprint.route('/api/items', methods=['GET'])
def get_all_items():
    response = requests.get('%s/api/item' % os.getenv('RESTAURANT_PATH')) 
    
    if response.status_code == 200:
        return jsonify(response.json()), response.status_code

    return response.status_code

@restaurant_blueprint.route('/api/item/<int:pk>', methods=['GET'])
def get_one_item(pk):
    response = requests.get(f'%s/api/item/{pk}' % os.getenv('RESTAURANT_PATH')) 
    
    data = response.json()

    if data['image']:
        data['image'] = f"http://restaurant.marques.rocks/api/item-image/{pk}"
    
    if response.status_code == 200:
        return jsonify(data), response.status_code

    return response.status_code


@restaurant_blueprint.route('/api/item/category', methods=['GET'])
def get_all_item_categories():
    response = requests.get('%s/api/item-category' % os.getenv('RESTAURANT_PATH'))

    if response.status_code == 200:
        return jsonify(response.json()), response.status_code

    return response.status_code

@restaurant_blueprint.route('/api/restaurant/category', methods=['GET'])
def get_all_restaurant_categories():
    response = requests.get('%s/api/restaurant-category' % os.getenv('RESTAURANT_PATH'))

    if response.status_code == 200:
        return jsonify(response.json()), response.status_code

    return response.status_code
