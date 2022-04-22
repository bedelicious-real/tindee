import hashlib
from dotenv import load_dotenv
from flask import Blueprint, request, jsonify
from api.middleware_auth import token_required
from api.gcp import upload_to_gcp
from database.db import TindeeUser, Mentee, Mentor
from helpers.logging import Logging

load_dotenv()
profile = Blueprint('profile', __name__)

def parse_image_from_request(req):
    Logging.print(req)
    file = req.files['file']
    return file.read()

@profile.route('/avatar', methods=['POST'])
@token_required
def upload_avatar(uuid, email):
    try:
        content = parse_image_from_request(request)
        md5 = hashlib.md5(content).hexdigest()
    except Exception as err:
        Logging.print(err)
        return jsonify('Cannot read image'), 400
    url = upload_to_gcp(content, md5)
    try:
        TindeeUser.updateUser(id=uuid, url=url)
    except Exception as err:
        print(err)
        return jsonify("We're not OK"), 500
    return jsonify('OK'), 200


@profile.route('', methods=['POST'])
@token_required
def upsert_profile(uuid, email):
    print(uuid, email)
    data = request.get_json()
    Logging.print(data)
    is_mentor = request.args.get('mentor', default=False, type=bool)
    if is_mentor:
        exp_years = data['years']               # int
        offers = data['offers']                 # array
        concentration = data['concentrations']  # array
        role = data['role']                     # str
        company_name = data['organization']     # str
    else:
        fulltime_status = data['status']        # str
        organization = data['organization']     # str
        education_level = data['level']         # str
        intro = data['intro']                   # str
    return jsonify('OK'), 200


@profile.route('', methods=['GET'])
@token_required
def get_profile(uuid, email):
    user_info = TindeeUser.userInfo(uuid)
    is_mentor = request.args.get('mentor', default=False, type=bool)
    try:
        if is_mentor:
            mentor_info = Mentor.mentorInfo(email)
            return jsonify({
                'email': email,
                'first-name': user_info['first_name'],
                'last-name': user_info['last_name'],
                'image-url': user_info['image_url'],
                'offers': mentor_info['offers'],
                'concentration': mentor_info['concentration'],
                'organization': mentor_info['company_id']   # please edit
            }), 200
        else:
            mentee_info = Mentee.menteeInfo(email)
            return jsonify({
                'email': email,
                'first-name': user_info['first_name'],
                'last-name': user_info['last_name'],
                'image-url': user_info['image_url'],
                'organization': mentee_info['organization'],
                'status': mentee_info['full_time_status'],
                'level': mentee_info['edu_level'],
                'intro': mentee_info['description']
            }), 200
    except Exception as err:
        Logging.print(err)
        return jsonify("We're not OK"), 500