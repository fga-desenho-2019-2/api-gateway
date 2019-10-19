from flask import Flask, jsonify, Blueprint, request
from flask_cors import CORS
import requests
import os

restaurant_blueprint = Blueprint('restaurant', __name__)
CORS(restaurant_blueprint)

