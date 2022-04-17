from flask import Flask
from api.user import user
from api.matches import matches
from database.db import db
# from database.match import db as match_db

app = Flask(__name__)
app.config.from_object('config.Config')
app.register_blueprint(user, url_prefix='/user')
app.register_blueprint(matches, url_prefix='/matches')

db.init_app(app)
# match_db.init_app(app)
app.app_context().push()
db.drop_all()
db.create_all()

