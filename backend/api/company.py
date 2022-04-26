from dotenv import load_dotenv
from flask import Blueprint, request, jsonify
from database.db import Company
from helpers.logging import Logging

load_dotenv()
company = Blueprint('company', __name__)

@company.route('', methods=['GET'])
def get_company():
    name = request.args.get('name', default='', type=str)
    Logging.print(name)
    try:
        id = Company.companyID(name)
        info = Company.companyInfo(id)
        
        return jsonify({
            'name': name,
            'description': info['description']
        }), 200
    except Exception as err:
        Logging.print(err)
        
        return jsonify({
            'name': name,
            'description': ''
        }), 200