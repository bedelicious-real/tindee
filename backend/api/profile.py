from flask import Blueprint, request
from middleware_auth import token_required

profile = Blueprint('profile', __name__)

def parse_image_from_request(req):
    return None

@profile.route('/avatar', methods=['POST'])
@token_required
def upload_avatar(uuid, email):
    image = parse_image_from_request(request)


@profile.route('/', methods=['POST'])
@token_required
def upsert_profile(uuid, email):
    pass


@profile.route('/', methods=['GET'])
@token_required
def get_profile(uuid, email):
    pass