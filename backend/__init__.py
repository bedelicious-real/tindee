from flask import Flask
from api.user import user

app = Flask(__name__)
app.register_blueprint(user, url_prefix='/user')