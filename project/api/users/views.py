from flask import Flask, jsonify, Blueprint, request
from flask_cors import CORS
import requests
import os

users_blueprint = Blueprint('users', __name__)
CORS(users_blueprint)