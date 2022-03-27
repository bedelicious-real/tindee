from flask import Flask
from database.db import db
from api.user import user

app = Flask(__name__)
app.register_blueprint(user, url_prefix='/user')

db.init_app(app)