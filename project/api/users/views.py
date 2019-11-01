from flask import Flask, jsonify, Blueprint, request
from flask_cors import CORS
import requests
import os

users_blueprint = Blueprint('users', __name__)
CORS(users_blueprint)

@users_blueprint.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    response = requests.post("%s/api/user/" % os.getenv('USERS_PATH'), json=data)
    return jsonify(response.json()), response.status_code

@users_blueprint.route('/user/<int:id>', methods=['GET'])
def get_user(id):
    response = requests.get("%s/api/user/%s" % (os.getenv('USERS_PATH'), id))
    return jsonify(response.json()), response.status_code

@users_blueprint.route('/user/list', methods=['GET'])
def get_all_users():
    response = requests.get("%s/api/user/list/" % (os.getenv('USERS_PATH')))
    return jsonify(response.json()), response.status_code

@users_blueprint.route('/auth/login', methods=['POST'])
def auth_user():
    data = request.get_json()
    response = requests.post("%s/api/token/" % os.getenv('USERS_PATH'), json=data)
    return jsonify(response.json()), response.status_code