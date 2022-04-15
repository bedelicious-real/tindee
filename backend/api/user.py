from datetime import timezone
import datetime
from dotenv import load_dotenv
from flask import Blueprint, request, current_app
import bcrypt
import os
import jwt
from database.db import TindeeUser

user = Blueprint('user', __name__)
load_dotenv()

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

    try:
        hashed_pwd = bcrypt.hashpw(
            raw_pwd, bcrypt.gensalt(rounds=SALT_ROUNDS)).decode()
        print(hashed_pwd)
        uuid = TindeeUser.insertUser(
            email, first_name, last_name, hashed_pwd, None)
        print(uuid)
        return jwt.encode(
            {
                'uuid': uuid,
                'email': email,
                'exp': datetime.datetime.now(tz=timezone.utc) + datetime.timedelta(hours=5)
            },
            JWT_SECRET_KEY,
            algorithm='HS256'
        )
    except Exception as err:
        print(err)
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
        if not bcrypt.checkpw(raw_pwd.encode(), hashed_pwd.encode()):
            return 'Wrong password', 400

        return jwt.encode(
            {
                'uuid': uuid,
                'email': email,
                'exp': datetime.datetime.now(tz=timezone.utc) + datetime.timedelta(hours=5)
            },
            JWT_SECRET_KEY,
            algorithm='HS256'
        )
    except Exception as err:
        print(err)
        return 'We\'re not OK', 500
