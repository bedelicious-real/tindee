from dotenv import load_dotenv
from flask import Blueprint
from api.middleware_auth import token_required
import os

matches = Blueprint('matches', __name__)

load_dotenv()
SALT_ROUNDS = int(os.environ.get('SALT_ROUNDS'))
JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')


@matches.route('/mentors', methods=['GET'])
@token_required
def get_mentors(uuid, email):
    pass


@matches.route('/mentees', methods=['GET'])
@token_required
def get_mentees(uuid, email):
    pass


@matches.route('/', methods=['POST'])
@token_required
def like(uuid, email):
    pass


@matches.route('/', methods=['DELETE'])
@token_required
def unlike(uuid, email):
    pass