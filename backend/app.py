from dotenv import load_dotenv
from flask import Flask
from api.user import user
from api.profile import profile
from api.matches import matches
from api.mentors import mentors
from database.db import db
# from database.match import db as match_db

from flask_cors import CORS

app = Flask(__name__)
app.config.from_object('config.Config')
CORS(app)
CORS(user)
CORS(profile)
CORS(matches)
CORS(mentors)
app.register_blueprint(user, url_prefix='/user')
app.register_blueprint(profile, url_prefix='/profile')
app.register_blueprint(matches, url_prefix='/matches')
app.register_blueprint(mentors, url_prefix='/mentors')

db.init_app(app)
# match_db.init_app(app)
app.app_context().push()
# db.drop_all()
# db.create_all()
