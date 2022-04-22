from dotenv import load_dotenv
from flask import Flask
from api.user import user
from api.profile import profile
from database.db import db

from flask_cors import CORS

app = Flask(__name__)
app.config.from_object('config.Config')
CORS(app)
CORS(user)
app.register_blueprint(user, url_prefix='/user')
app.register_blueprint(profile, url_prefix='/profile')

db.init_app(app)
app.app_context().push()
# db.drop_all()
# db.create_all()
