from functools import wraps
import requests
import os
from flask import request, jsonify

def get_auth_status(request):
    auth_bearer = request.headers.get('Authorization')

    if not auth_bearer:
        response = {
            'is_logged': False,
            'error': {
                'content': {
                    'status': 'fail',
                    'message': 'Unauthorized'
                },
                'status_code': 401
            }
        }
        return response

    token = {'token': auth_bearer}
    auth_response = requests.post("%s/api/token/verify/" % os.getenv('USERS_PATH'), json=token)

    if auth_response.status_code != 200:
        response = {
            'is_logged': False,
            'error': {
                'content': auth_response.json(),
                'status_code': auth_response.status_code
            }
        }
        return response
    else:
        response = {
            'is_logged': True
        }
        return response

def needs_auth(f):
    @wraps(f)
    def decorates_function(*args, **kwargs):
        auth_status = get_auth_status(request)

        if not auth_status.get('is_logged'):
            return jsonify(auth_status.get('error').get('content')), auth_status.get('error').get('status_code')

        return f(*args, **kwargs)

    return decorates_function