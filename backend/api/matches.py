from multiprocessing import dummy
from flask import Blueprint, request, jsonify
from dotenv import load_dotenv
from flask import Blueprint, request
from api.middleware_auth import token_required
from database.db import Company, Mentor
from database.match import Like, Match
import os

from api.middleware_auth import token_required

matches = Blueprint('matches', __name__)

load_dotenv()
SALT_ROUNDS = int(os.environ.get('SALT_ROUNDS'))
JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
SHORTENED_LIST_LEN = 20

@matches.route('/mentors', methods=['GET'])
@token_required
def get_mentors_list(uuid, email):
    is_full = request.args.get('full', default=False, type=bool)
    # dummy_mentor = {
    #     'email': 'a@x.com',
    #     'first-name': 'First',
    #     'last-name': 'Last',
    #     'image-url': 'https://storage.googleapis.com/tindee/avatar/7f04ec92b8198cd9b36d8d9a6f343476.png',
    #     'organization': 'Bkav',
    #     'concentration': ['Backend', 'Frontend'],
    #     'offers': ['Mock Interview', 'Love']
    # }
    email_lists = Match.getMentors(email)
    mentors = []
    for mentor_email in email_lists:
        if not is_full and len(mentors) > SHORTENED_LIST_LEN:
            break
        
        info = Mentor.mentorInfo(mentor_email)
        company_info = Company.companyInfo(info['company_id'])
        mentors.append({
            'email': mentor_email,
            'first-name': info['first_name'],
            'last-name': info['last_name'],
            'image-url': info['image_url'],
            'organization': company_info['name'],
            'offers': info['offers'],
            'concentration': info['concentration'],
        })


    return jsonify(mentors), 200

@matches.route('/mentees', methods=['GET'])
@token_required
def get_mentees_list(uuid, email):
    is_full = request.args.get('full', default=False, type=bool)
    # dummy_mentee = {
    #     'email': 'a@x.com',
    #     'first-name': 'First',
    #     'last-name': 'Last',
    #     'image-url': 'https://storage.googleapis.com/tindee/avatar/7f04ec92b8198cd9b36d8d9a6f343476.png',
    #     'organization': 'Bkav',
    #     'status': 'CEO',
    #     'level': 'PhD',
    #     'intro': 'Here is my intro. Thank you so much!'
    # }
    email_lists = Match.getMentees(email)
    mentees = []
    for mentee_email in email_lists:
        if not is_full and len(mentees) > SHORTENED_LIST_LEN:
            break

        info = Mentor.mentorInfo(mentee_email)
        mentees.append({
            'email': mentee_email,
            'first-name': info['first_name'],
            'last-name': info['last_name'],
            'image-url': info['image_url'],
            'organization': info['organization'],
            'status': info['full_time_status'],
            'level': info['edu_level'],
            'intro': info['description']
        })

    return jsonify(mentees), 200


@matches.route('', methods=['POST'])
@token_required
def like(uuid, email):
    matched = False
    try:
        response = True
        target_email = request.get_json()
        response &= Like.insertLike(email, target_email)

        if response and Like.isMatch(email, target_email):
            if Mentor.isMentor(target_email): 
                email, target_email = target_email, email
            response &= Match.insertMatch(email, target_email)
            matched = True
        
        if response == False:
            return jsonify("We're not OK"), 500
    except Exception:
        return jsonify("We're not OK"), 500

    return jsonify("Matched" if matched else "Liked"), 200


@matches.route('', methods=['DELETE'])
@token_required
def unlike(uuid, email):
    target_email = request.get_json()
    try:
        response = Like.deleteLike(email, target_email)
        if response == False:
            return jsonify("We're not OK"), 500
    except Exception:
        return jsonify("We're not OK"), 500

    return jsonify('OK'), 200