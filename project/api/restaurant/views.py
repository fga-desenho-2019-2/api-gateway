from flask import Flask, jsonify, Blueprint, request
from flask_cors import CORS
import requests
import os

restaurant_blueprint = Blueprint('restaurant', __name__)
CORS(restaurant_blueprint)

@restaurant_blueprint.route('/api/restaurants', methods=['GET'])
def get_restaurants():
    response = requests.get('%s/api/restaurant' % os.getenv('RESTAURANT_PATH'))

    return jsonify(response.json()), 200
