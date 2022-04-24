from dotenv import load_dotenv
from flask import Blueprint, request, jsonify
from api.middleware_auth import token_required
from database.db import Company
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
    
    result = engine.result()
    mentors = []
    for ele in result:
        company_info = Company.companyInfo(ele['company_id'])
        mentors.append({
            'email': ele['email'],
            'first-name': ele['first_name'],
            'last-name': ele['last_name'],
            'image-url': ele['image_url'],
            'years': ele['exp_years'],
            'offers': ele['offers'],
            'concentration': ele['concentration'],
            'organization': company_info['name']
        })

    return jsonify(mentors), 200
