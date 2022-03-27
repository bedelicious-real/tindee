from flask import Flask
from api.user import user
from database.db import db

app = Flask(__name__)
app.config.from_object('config.Config')
app.register_blueprint(user, url_prefix='/user')

db.init_app(app)