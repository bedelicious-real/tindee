from crypt import methods
from datetime import timezone
import datetime
from dotenv import load_dotenv
from flask import Blueprint, request, current_app, jsonify
import bcrypt
import os
import jwt
from database.db import TindeeUser

from flask_cors import CORS, cross_origin

user = Blueprint('user', __name__)
load_dotenv()

load_dotenv()
SALT_ROUNDS = int(os.environ.get('SALT_ROUNDS'))
JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')

@user.route('', methods=['GET'])
def test():
    return jsonify('OK'), 200

@user.route('', methods=['POST'])
@cross_origin()
def create_new_user():
    data = request.get_json()
    if data is None:
        return jsonify('There is no data to process'), 400

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
        return jsonify(jwt.encode(
            {
                'uuid': uuid,
                'email': email,
                'exp': datetime.datetime.now(tz=timezone.utc) + datetime.timedelta(hours=5)
            },
            JWT_SECRET_KEY,
            algorithm='HS256'
        ))
    except Exception as err:
        print(err)
        if str(err) == 'Existed':
            return jsonify('User already existed'), 400
        if str(err) == 'Other':
            return jsonify('We\'re not OK'), 500


@user.route('/session', methods=['POST'])
@cross_origin()
def login():
    data = request.get_json()
    print(data)
    if data is None:
        return jsonify('There is no data to process'), 400

    email = data['email']
    raw_pwd = data['pwd']
    try:
        uuid = TindeeUser.searchUUID(email)
        if uuid is None:
            return jsonify('User not found'), 404
        hashed_pwd = TindeeUser.searchHashpass(uuid)
        if not bcrypt.checkpw(raw_pwd.encode(), hashed_pwd.encode()):
            return jsonify('Wrong password'), 400

        return jsonify(jwt.encode(
            {
                'uuid': uuid,
                'email': email,
                'exp': datetime.datetime.now(tz=timezone.utc) + datetime.timedelta(hours=5)
            },
            JWT_SECRET_KEY,
            algorithm='HS256'
        ))
    except Exception as err:
        print(err)
        return jsonify('We\'re not OK'), 500
