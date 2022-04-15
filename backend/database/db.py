from sqlite3 import IntegrityError
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
    hashpass = db.Column(db.String(500), nullable=False)
    image_url = db.Column(db.String(500))

    def __init__(self, email, first_name, last_name, hashpass, url):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.hashpass = hashpass
        self.image_url = url

    @staticmethod
    def searchHashpass(id):
        user = TindeeUser.query.filter_by(uuid=id).first()
        return None if user == None else user.hashpass

    @staticmethod
    def searchUUID(findEmail):
        user = TindeeUser.query.filter_by(email=findEmail).first()
        return None if user == None else str(user.uuid)

    @staticmethod
    def insertUser(email, first_name, last_name, hashpass, image_url):
        newUser = TindeeUser(email, first_name, last_name, hashpass, image_url)
        db.session.add(newUser)
        try:
            db.session.commit()
            print(TindeeUser.searchUUID(email))
            return TindeeUser.searchUUID(email)
        except IntegrityError as ie:
            print(ie)
            raise Exception('Existed')
        except Exception as e:
            print(e)
            raise Exception('Other')

    @staticmethod
    def updateIMGURL(id, url):
        user = TindeeUser.query.filter_by(uuid=id).first()
        if (user is None):
            raise Exception('Nonexistent')
        user.image_url = url
        db.session.commit()
