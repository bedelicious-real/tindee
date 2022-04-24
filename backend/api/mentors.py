from dotenv import load_dotenv
from flask import Blueprint, request, jsonify
from api.middleware_auth import token_required
from database.search import Search

mentors = Blueprint('mentors', __name__)

load_dotenv()

@mentors.route('', methods=['POST'])
@token_required
def search_mentors(uuid, email):
    engine = Search()
    queries = request.get_json()
    for query in queries:
        key, val = query['type'], query['value']
        if key == 'first-name':
            engine = engine.search_by_first_name(val)
        elif key == 'last-name':
            engine = engine.search_by_last_name(val)
        elif key == 'offers':
            engine = engine.search_by_offers(val)
        elif key == 'concentration':
            engine = engine.search_by_concentrations(val)
    
    print(engine.result())

    return jsonify('OK'), 200
