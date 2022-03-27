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
        print(TindeeUser.query.first())
        return TindeeUser.query.filter_by(uuid=id).first().hashpass

    @staticmethod
    def searchUUID(findEmail):
        return TindeeUser.query.filter_by(email=findEmail).first().uuid

    @staticmethod
    def insertUser(email, first_name, last_name, hashpass, image_url):
        newUser = TindeeUser(email, first_name, last_name, hashpass, image_url)
        db.session.add(newUser)
        try:
            db.session.commit()
            return True
        except IntegrityError as ie:
            print(ie)
            raise Exception('Existed')
        except Exception as e:
            print(e)
            raise Exception('Other')
