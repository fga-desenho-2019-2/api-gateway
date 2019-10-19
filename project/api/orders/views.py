from flask import Flask, jsonify, Blueprint, request
from flask_cors import CORS
import requests
import os

orders_blueprint = Blueprint('orders', __name__)
CORS(orders_blueprint)
