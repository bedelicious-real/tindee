from dotenv import load_dotenv
from flask import Blueprint, request
from api.middleware_auth import token_required
from database.match import Like, Match
import os

matches = Blueprint('matches', __name__)

load_dotenv()
SALT_ROUNDS = int(os.environ.get('SALT_ROUNDS'))
JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')


@matches.route('/mentors', methods=['GET'])
@token_required
def get_mentors(uuid, email):
    is_full = request.args.get('full', default=False, type=bool)
    return 200


@matches.route('/mentees', methods=['GET'])
@token_required
def get_mentees(uuid, email):
    is_full = request.args.get('full', default=False, type=bool)
    return 200


@matches.route('/', methods=['POST'])
@token_required
def like(uuid, email):
    try:
        response = True
        receiver = request.get_json()
        response &= Like.insertLike(email, receiver)
        if response and Like.isMatch(email, receiver):
            response &= Match.insertMatch(email, receiver)
        
        if response == False:
            return 'We\'re not OK', 500
    except Exception:
        return 'We\'re not OK', 500

    return 'Very OK', 200


@matches.route('/', methods=['DELETE'])
@token_required
def unlike(uuid, email):
    receiver = request.get_json()
    try:
        response = Like.deleteLike(email, receiver)
        if response == False:
            return 'We\'re not OK', 500
    except Exception:
        return 'We\'re not OK', 500

    return 'Very OK', 200