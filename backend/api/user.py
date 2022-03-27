from flask import Blueprint, request, current_app
import bcrypt
import os
import jwt
from database.db import TindeeUser

user = Blueprint('user', __name__)

SALT_ROUNDS = int(os.environ.get('SALT_ROUNDS'))
JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')

@user.route('/', methods=['POST'])
def create_new_user():
    data = request.get_json()
    if data is None:
        return 'There is no data to process', 400
    
    email = data['email']
    first_name = data['first']
    last_name = data['last']
    raw_pwd = data['pwd'].encode()
    hashed_pwd = bcrypt.hashpw(raw_pwd, bcrypt.gensalt(rounds=SALT_ROUNDS))
    
    try:
        uuid = TindeeUser.insertUser(email, first_name, last_name, hashed_pwd, None)
        return jwt.encode(
            {
                'uuid': uuid,
                'email': email
            }, 
            JWT_SECRET_KEY,
            algorithm='HS256'
        )
    except Exception as err:
        if str(err) == 'Existed':
            return 'User already existed', 400
        if str(err) == 'Other':
            return 'We\'re not OK', 500 


@user.route('/session', methods=['POST'])
def login():
    data = request.get_json()
    print(data)
    if data is None:
        return 'There is no data to process', 400
    
    email = data['email']
    raw_pwd = data['pwd']
    try:
        uuid = TindeeUser.searchUUID(email)
        if uuid is None:
            return 'User not found', 404
        hashed_pwd = TindeeUser.searchHashpass(uuid)
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
    except Exception as err:
        print(err)
        return 'We\'re not OK', 500