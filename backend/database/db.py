from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID
import uuid as uid

db = SQLAlchemy()


class TindeeUser(db.Model):
    uuid = db.Column(UUID(as_uuid=True), primary_key=True, default=uid.uuid4)
    email = db.Column(db.String(50), unique=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    hashpass = db.Column(db.String(50), nullable=False)
    image_url = db.Column(db.String(50), nullable=False)

    def searchHashpass(id):
        return TindeeUser.query.filter_by(uuid=id).first().hashpass
