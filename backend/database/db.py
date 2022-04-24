from sqlite3 import IntegrityError
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid as uid

db = SQLAlchemy()

# General user of Tindee


class TindeeUser(db.Model):
    __tablename__ = 'tindeeUser'
    uuid = db.Column(UUID(as_uuid=True), primary_key=True, default=uid.uuid4)
    email = db.Column(db.String(50), unique=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    hashpass = db.Column(db.String(500), nullable=False)
    image_url = db.Column(db.String(500))
    # relationship to mentor
    mentor = db.relationship('Mentor', back_populates='user', uselist=False)
    # relationship to mentee
    mentee = db.relationship('Mentee', back_populates='user', uselist=False)

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
        print('hoho')
        db.session.add(newUser)
        print('cac')
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
    def updateUser(id, first_name=None, last_name=None, url=None):
        user = TindeeUser.query.filter_by(uuid=id).first()
        if (user is None):
            raise Exception('Nonexistent')
        if (url is not None):
            user.image_url = url
        if (first_name is not None):
            user.first_name = first_name
        if (last_name is not None):
            user.last_name = last_name
        try:
            db.session.commit()
            return id
        except IntegrityError as integrity:
            raise Exception('Integrity Vioalation')
        except Exception as e:
            raise Exception('Other')

    @staticmethod
    def userInfo(id):
        user = TindeeUser.query.filter_by(uuid=id).first()
        if (user is None):
            raise Exception('Nonexistent')
        return {'email': user.email, 'first_name': user.first_name,
                'last_name': user.last_name, 'image_url': user.image_url}

# Mentor user of Tindee


class Mentor(db.Model):
    __tablename__ = 'mentor'
    email = db.Column(db.String(50), ForeignKey(
        'tindeeUser.email'), primary_key=True, nullable=False)
    exp_years = db.Column(db.Integer, nullable=False)
    offers = db.Column(db.ARRAY(db.String(100)), nullable=False)
    concentration = db.Column(db.ARRAY(db.String(100)), nullable=False)
    company_id = db.Column(db.Integer, nullable=False)
    role = db.Column(db.String(100), nullable=False)

    # Foreign key to TindeeUser
    user = db.relationship('TindeeUser', back_populates='mentor')

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
    def updateMentor(mentorEmail, exp_years, offers, concentration, role, company_id):
        mentor = Mentor.query.filter_by(email=mentorEmail).first()
        if (mentor is None):
            return Mentor.insertMentor(mentorEmail, exp_years, offers, concentration, company_id)
        else:
            mentor.exp_years = exp_years
            mentor.offers = offers
            mentor.concentration = concentration
            mentor.company_id = company_id
            try:
                db.session.commit()
                return mentorEmail
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

# Mentee user of Tindee


class Mentee(db.Model):
    __tablename__ = 'mentee'
    email = db.Column(db.String(50), ForeignKey(
        'tindeeUser.email'), primary_key=True, nullable=False)
    organization = db.Column(db.String(100), nullable=False)
    full_time_status = db.Column(db.String(100), nullable=False)
    edu_level = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(1000), nullable=False)

    # Foreign key to TindeeUser
    user = db.relationship('TindeeUser', back_populates='mentee')

    def __init__(self, email, organization, full_time_status, edu_level, description):
        self.email = email
        self.organization = organization
        self.full_time_status = full_time_status
        self.edu_level = edu_level
        self.description = description

    @staticmethod
    def insertMentee(email, organization, full_time_status, edu_level, description):
        newMentee = Mentee(email, organization,
                           full_time_status, edu_level, description)
        db.session.add(newMentee)
        try:
            db.session.commit()
            return email
        except IntegrityError as integrity:
            raise Exception('Integrity Vioalation')
        except Exception as e:
            raise Exception('Other')

    @staticmethod
    def updateMentee(menteeEmail, organization, full_time_status, edu_level, description):
        mentee = Mentee.query.filter_by(email=menteeEmail).first()
        if (mentee is None):
            return Mentee.insertMentee(menteeEmail, organization, full_time_status, edu_level, description)
        else:
            mentee.organization = organization
            mentee.full_time_status = full_time_status
            mentee.edu_level = edu_level
            mentee.description = description
            try:
                db.session.commit()
                return menteeEmail
            except IntegrityError as integrity:
                raise Exception('Integrity Vioalation')
            except Exception as e:
                raise Exception('Other')

    @staticmethod
    def menteeInfo(menteeEmail):
        mentee = Mentee.query.filter_by(email=menteeEmail).first()
        if (mentee is None):
            raise Exception('Nonexistent')
        return {'first_name': mentee.first_name, 'last_name': mentee.last_name,
                'image_url': mentee.image_url, 'organization': mentee.organization,
                'full_time_status': mentee.full_time_status, 'edu_level': mentee.edu_level,
                'description': mentee.description}
