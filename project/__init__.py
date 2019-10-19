import os
from flask import Flask, jsonify

from project.api.orders.views import orders_blueprint
from project.api.payment.views import payment_blueprint
from project.api.restaurant.views import restaurant_blueprint
from project.api.users.views import users_blueprint


def create_app():

    app = Flask(__name__)

    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    app.register_blueprint(orders_blueprint)
    app.register_blueprint(payment_blueprint)
    app.register_blueprint(restaurant_blueprint)
    app.register_blueprint(users_blueprint)

    return app