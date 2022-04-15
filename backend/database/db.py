from sqlite3 import IntegrityError
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid as uid

db = SQLAlchemy()

# General user of Tindee


class TindeeUser(db.Model):
    uuid = db.Column(UUID(as_uuid=True), primary_key=True, default=uid.uuid4)
    email = db.Column(db.String(50), unique=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    hashpass = db.Column(db.String(500), nullable=False)
    image_url = db.Column(db.String(500))
    mentor = db.relationship('Mentor', back_populates='user', uselist=False)

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

# Mentor user of Tindee


class Mentor(db.Model):
    email = db.Column(db.String(50), ForeignKey(
        'user.email'), primary_key=True, nullable=False)
    exp_years = db.Column(db.Integer, nullable=False)
    offers = db.Column(db.ARRAY(db.String(100)), nullable=False)
    concentration = db.Column(db.ARRAY(db.String(100)), nullable=False)
    company_id = db.Column(db.Integer, nullable=False)

    # Foreign key to TindeeUser
    user = db.relationship('User', back_populates='mentor')

    def __init__(self, email, exp_years, offers, concentration, company_id):
        self.email = email
        self.exp_years = exp_years
        self.offers = offers
        self.concentration = concentration
        self.company_id = company_id

    @staticmethod
    def insertMentor(email, exp_years, offers, concentration, company_id):
        newMentor = Mentor(email, exp_years, offers, concentration, company_id)
        db.session.add(newMentor)
        try:
            db.session.commit()
            return email
        except IntegrityError as integrity:
            raise Exception('Integrity Vioalation')
        except Exception as e:
            raise Exception('Other')

    @staticmethod
    def mentorInfo(mentorEmail):
        mentor = Mentor.query.filter_by(email=mentorEmail).first()
        if (mentor is None):
            raise Exception('Nonexistent')
        return {'first_name': mentor.first_name, 'last_name': mentor.last_name,
                'image_url': mentor.image_url, 'exp_years': mentor.exp_years,
                'offers': mentor.offers, 'concentration': mentor.concentration,
                'company_id': mentor.company_id}
