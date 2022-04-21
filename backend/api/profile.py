from dotenv import load_dotenv
from flask import Blueprint, request
from api.middleware_auth import token_required
from api.gcp import upload_to_gcp
from database.db import TindeeUser, Mentee, Mentor

load_dotenv()
profile = Blueprint('profile', __name__)

def parse_image_from_request(req):
    f = open('/Users/trungnguyen/Downloads/img-0001.png', 'rb')
    return f.read()

@profile.route('/avatar', methods=['POST'])
@token_required
def upload_avatar(uuid, email):
    content = parse_image_from_request(request)
    url = upload_to_gcp(content)
    print(uuid, email, url)
    try:
        TindeeUser.updateUser(id=uuid, url=url)
    except Exception as err:
        print(err)
        return 'Khok', 500
    return 'uWu', 200


@profile.route('/', methods=['POST'])
@token_required
def upsert_profile(uuid, email):
    pass


@profile.route('/', methods=['GET'])
@token_required
def get_profile(uuid, email):
    pass