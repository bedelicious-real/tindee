from flask import Blueprint, request
from middleware_auth import token_required
from gcp import upload_to_gcp

profile = Blueprint('profile', __name__)

def parse_image_from_request(req):
    f = open('/Users/trungnguyen/Downloads/img-0001.png', 'rb')
    return f.read()

@profile.route('/avatar', methods=['POST'])
@token_required
def upload_avatar(uuid, email):
    content = parse_image_from_request(request)
    url = upload_to_gcp(content)
    return 'uWu', 200


@profile.route('/', methods=['POST'])
@token_required
def upsert_profile(uuid, email):
    pass


@profile.route('/', methods=['GET'])
@token_required
def get_profile(uuid, email):
    pass