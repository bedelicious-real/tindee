from multiprocessing import dummy
from flask import Blueprint, request, jsonify

from api.middleware_auth import token_required

matches = Blueprint('matches', __name__)

@matches.route('/mentors', methods=['GET'])
@token_required
def get_mentors_list(uuid, email):
    is_full = request.args.get('full', default=False, type=bool)
    dummy_mentor = {
        'email': 'a@x.com',
        'first-name': 'First',
        'last-name': 'Last',
        'image-url': 'https://storage.googleapis.com/tindee/avatar/7f04ec92b8198cd9b36d8d9a6f343476.png',
        'organization': 'Bkav',
        'concentration': ['Backend', 'Frontend'],
        'offers': ['Mock Interview', 'Love']
    }

    return jsonify([dummy_mentor]), 200


@matches.route('/mentees', methods=['GET'])
@token_required
def get_mentees_list(uuid, email):
    is_full = request.args.get('full', default=False, type=bool)
    dummy_mentee = {
        'email': 'a@x.com',
        'first-name': 'First',
        'last-name': 'Last',
        'image-url': 'https://storage.googleapis.com/tindee/avatar/7f04ec92b8198cd9b36d8d9a6f343476.png',
        'organization': 'Bkav',
        'status': 'CEO',
        'level': 'PhD',
        'intro': 'Here is my intro. Thank you so much!'
    }

    return jsonify([dummy_mentee]), 200


@matches.route('', methods=['POST'])
@token_required
def like(uuid, email):
    target_email = request.get_json()

    return jsonify('OK'), 200


@matches.route('', methods=['DELETE'])
@token_required
def unlike(uuid, email):
    target_email = request.get_json()

    return jsonify('OK'), 200
