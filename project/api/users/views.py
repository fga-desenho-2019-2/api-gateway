from flask import Flask, jsonify, Blueprint, request
from flask_cors import CORS
import requests
import os

from project.api.shared.auth_utils import needs_auth

users_blueprint = Blueprint('users', __name__)
CORS(users_blueprint)

@users_blueprint.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    response = requests.post("%s/api/user/" % os.getenv('USERS_PATH'), json=data)
    return jsonify(response.json()), response.status_code

@users_blueprint.route('/user/<cpf>', methods=['GET'])
@needs_auth
def get_user(cpf):
    response = requests.get("%s/api/get_user/%s" % (os.getenv('USERS_PATH'), cpf))
    return jsonify(response.json()), response.status_code

@users_blueprint.route('/user/<cpf>', methods=['PUT'])
@needs_auth
def put_user(cpf):
    data = request.get_json()
    response = requests.put("%s/api/edit_user/%s" % (os.getenv('USERS_PATH'), cpf), json=data)
    return jsonify(response.json()), response.status_code

@users_blueprint.route('/user/list', methods=['GET'])
@needs_auth
def get_all_users():
    response = requests.get("%s/api/user/list/" % (os.getenv('USERS_PATH')))
    return jsonify(response.json()), response.status_code

@users_blueprint.route('/auth/login', methods=['POST'])
def auth_user():
    data = request.get_json()
    response = requests.post("%s/api/token/" % os.getenv('USERS_PATH'), json=data)
    return jsonify(response.json()), response.status_code