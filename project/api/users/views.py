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
    print(response.text)
    return jsonify(response.json()), response.status_code

@users_blueprint.route('/get_user/<string:cpf>', methods=['GET'])
@needs_auth
def get_user(cpf):
    response = requests.get("%s/api/get_user/%s" % (os.getenv('USERS_PATH'), cpf))
    return jsonify(response.json()), response.status_code

@users_blueprint.route('/edit_user/<string:cpf>', methods=['PUT'])
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

@users_blueprint.route('/user/post_image', methods=['POST'])
@needs_auth
def create_user_image():
    data = request.get_json()
    response = requests.post("%s/api/user/post_image" % os.getenv('USERS_PATH'), json=data)
    return jsonify(response.json()), response.status_code

@users_blueprint.route('/user/get_image/<string:cpf>', methods=['GET'])
@needs_auth
def get_user_image(cpf):
    response = requests.get("%s/api/user/get_image/%s" % (os.getenv('USERS_PATH'), cpf))
    return jsonify(response.json()), response.status_code

@users_blueprint.route('/user/delete_image/<string:cpf>/', methods=['DELETE'])
@needs_auth
def delete_user_image(cpf):
    response = requests.get("%s/user/delete_image/%s" % (os.getenv('USERS_PATH'), cpf))
    return jsonify(response.json()), response.status_code

cards_blueprint = Blueprint('users', __name__)
CORS(cards_blueprint)

@cards_blueprint.route('/user/card', methods=['POST'])
def create_card():
    data = request.get_json()
    response = requests.post("%s/api/user/card" % os.getenv('USERS_PATH'), json=data)
    return jsonify(response.json()), response.status_code

@cards_blueprint.route('/user/card/<int:id>', methods=['GET'])
@needs_auth
def get_card(id):
    response = requests.get("%s/api/user/card/%s" % (os.getenv('USERS_PATH'), id))
    return jsonify(response.json()), response.status_code

@cards_blueprint.route('/user/card/<int:id>', methods=['PUT'])
@needs_auth
def put_card(id):
    response = requests.put("%s/api/user/card/%s" % (os.getenv('USERS_PATH'), id))
    return jsonify(response.json()), response.status_code

@cards_blueprint.route('/user/card/<int:id>', methods=['DELETE'])
@needs_auth
def delete_card(id):
    response = requests.put("%s/api/user/card/%s" % (os.getenv('USERS_PATH'), id))
    return jsonify(response.json()), response.status_code

@cards_blueprint.route('/user/user_cards/', methods=['GET'])
@needs_auth
def get_user_cards(cpf):
    response = requests.get("%s/user/user_cards/%s" % (os.getenv('USERS_PATH'), cpf))
    return jsonify(response.json()), response.status_code


