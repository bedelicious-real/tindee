from functools import wraps
import os
from flask import request
import jwt

SALT_ROUNDS = int(os.environ.get('SALT_ROUNDS'))
JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'Authorization' not in request.headers:
            return "Token is missing", 400
        
        try:
            token = request.headers['Authorization'].split(' ')[1]
            user_info = jwt.decode(token, JWT_SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return 'Token is expired', 400
        except Exception as err:
            print(err)
            return 'Cannot verify user', 400

        return f(user_info['uuid'], user_info['email'], *args, **kwargs)


    return decorated


