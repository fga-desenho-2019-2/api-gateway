from flask import Flask, jsonify, Blueprint, request
from flask_cors import CORS
import requests
import os

payment_blueprint = Blueprint('payment', __name__)
CORS(payment_blueprint)