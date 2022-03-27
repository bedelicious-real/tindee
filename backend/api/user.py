from flask import Blueprint, request
import bcrypt
import os
import jwt

user = Blueprint('user', __name__)

SALT_ROUNDS = os.environ.get('SALT_ROUNDS')
JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')

@user.route('/', methods=['GET'])
def test():
    return 'Hahaha'

@user.route('/', methods=['POST'])
def create_new_user():
    data = request.get_json()
    if data is None:
        return 'There is no data to process', 400
    
    email = data['email']
    first_name = data['first']
    last_name = data['last']
    raw_pwd = data['pwd']
    hashed_pwd = bcrypt.hashpw(raw_pwd, bcrypt.gensalt(rounds=SALT_ROUNDS))
    
    return 'Ulatr', 200


@user.route('/session', methods=['POST'])
def login():
    data = request.get_json()
    if data is None:
        return 'There is no data to process', 400
    
    email = data['email']
    raw_pwd = data['pwd']
    uuid = 'CHANGE!!'
    hashed_pwd = 'CHANGE!!'
    if not bcrypt.checkpw(raw_pwd, hashed_pwd):
        return 'Wrong password', 400
    
    return jwt.encode(
        {
            'uuid': uuid,
            'email': email
        }, 
        JWT_SECRET_KEY,
        algorithm='HS256'
    )