import email
from sqlite3 import IntegrityError
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import UUID
db = SQLAlchemy()
# from database.work import Job, Company
import uuid as uid
from sqlalchemy.orm import backref as bf


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
    # mentor = db.relationship('Mentor', back_populates='user', uselist=False)
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
        print("HiHi")
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
    role = db.Column(db.String(100), nullable=False)
    company_id = db.Column(UUID(as_uuid=True), ForeignKey(
        'company.company_id'), nullable=False)

    # Foreign key to TindeeUser
    user = db.relationship('TindeeUser', backref=bf(
        'mentor', uselist=False), foreign_keys='[Mentor.email]')

    # Foreign key to Company
    company = db.relationship('Company', backref=bf(
        'mentor', uselist=False), foreign_keys='[Mentor.company_id]')

    def __init__(self, email, exp_years, offers, concentration, role, company_id):
        self.email = email
        self.exp_years = exp_years
        self.offers = offers
        self.concentration = concentration
        self.role = role
        self.company_id = company_id

    @staticmethod
    def insertMentor(email, exp_years, offers, concentration, role, company_id):
        newMentor = Mentor(email, exp_years, offers, concentration, role, company_id)
        db.session.add(newMentor)
        try:
            db.session.commit()
            return email
        except IntegrityError as integrity:
            print(integrity)
            raise Exception('Integrity Vioalation')
        except Exception as e:
            print(e)
            raise Exception('Other')

    @staticmethod
    def updateMentor(mentorEmail, exp_years, offers, concentration, role, company_id):
        mentor = Mentor.query.filter_by(email=mentorEmail).first()
        if (mentor is None):
            return Mentor.insertMentor(mentorEmail, exp_years, offers, concentration, role, company_id)
        else:
            if (exp_years is not None):
                mentor.exp_years = exp_years
            if (offers is not None):
                mentor.offers = offers
            if (concentration is not None):
                mentor.concentration = concentration
            if (company_id is not None):
                mentor.company_id = company_id
            if (role is not None):
                mentor.role = role
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
        return {'first_name': mentor.user.first_name, 'last_name': mentor.user.last_name,
                'image_url': mentor.user.image_url, 'exp_years': mentor.exp_years,
                'offers': mentor.offers, 'concentration': mentor.concentration,
                'company_id': mentor.company_id}

    @staticmethod
    def isMentor(mentorEmail):
        mentor = Mentor.query.filter_by(email=mentorEmail).first()
        return mentor is not None
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
            if (organization is not None):
                mentee.organization = organization
            if (full_time_status is not None):
                mentee.full_time_status = full_time_status
            if (edu_level is not None):
                mentee.edu_level = edu_level
            if (description is not None):
                mentee.description = description
            try:
                db.session.commit()
                return menteeEmail
            except IntegrityError as integrity:
                print(integrity)
                raise Exception('Integrity Vioalation')
            except Exception as e:
                print(e)
                raise Exception('Other')

    @staticmethod
    def menteeInfo(menteeEmail):
        mentee = Mentee.query.filter_by(email=menteeEmail).first()
        if (mentee is None):
            raise Exception('Nonexistent')
        return {'first_name': mentee.user.first_name, 'last_name': mentee.user.last_name,
                'image_url': mentee.user.image_url, 'organization': mentee.organization,
                'full_time_status': mentee.full_time_status, 'edu_level': mentee.edu_level,
                'description': mentee.description}

    @staticmethod
    def isMentee(menteeEmail):
        mentee = Mentee.query.filter_by(email=menteeEmail).first()
        return mentee is not None

class Job(db.Model):
    __tablename__ = 'job'
    email = db.Column(db.String(50), db.ForeignKey(
        'tindeeUser.email'), primary_key=True, nullable=False)
    job_name = db.Column(db.String(100), primary_key=True, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    annual_salary = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(1000), nullable=False)

    user = db.relationship('TindeeUser', backref=bf(
        'job', uselist=False), foreign_keys='[Job.email]')

    def __init__(self, email, job_name, location, annual_salary, description):
        self.email = email
        self.job_name = job_name
        self.location = location
        self.annual_salary = annual_salary
        self.description = description

    @staticmethod
    def insertJob(email, job_name, location, annual_salary, description):
        newJob = Job(email, job_name, location, annual_salary, description)
        db.session.add(newJob)
        try:
            db.session.commit()
            return True
        except IntegrityError as ie:
            print(ie)
            return False
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def updateJob(mentor_email, mentor_job_name, location, annual_salary, description):
        job = Job.query.filter_by(email=mentor_email, job_name=mentor_job_name)
        if (job is None):
            return Job.insertJob(mentor_email, mentor_job_name, location, annual_salary, description)
        if (location is not None):
            job.location = location
        if (annual_salary is not None):
            job.annual_salary = annual_salary
        if (description is not None):
            job.description = description
        try:
            db.session.commit()
            return True
        except IntegrityError as ie:
            print(ie)
            return False
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def deleteJob(mentor_email, mentor_job_name):
        job = Job.query.filter_by(email=mentor_email, job_name=mentor_job_name)
        db.session.delete(job)
        try:
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def jobInfo(mentor_email, mentor_job_name):
        job = Job.query.filter_by(
            email=mentor_email, job_name=mentor_job_name).first()
        if (job is None):
            raise Exception('Nonexistent')
        return {'email': job.email, 'job_name': job.job_name,
                'location': job.location, 'annual_salary': job.annual_salary,
                'description': job.description}


class Company(db.Model):
    __tablename__ = 'company'
    company_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uid.uuid4)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(1000), nullable=False)

    def __init__(self, name, description):
        self.name = name
        self.description = description

    @staticmethod
    def insertCompany(name, description):
        newCompany = Company(name, description)
        db.session.add(newCompany)
        try:
            db.session.commit()
            return True
        except IntegrityError as ie:
            print(ie)
            return False
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def updateCompany(id, name, description):
        company = Company.query.filter_by(company_id=id)
        if (company is None):
            return Company.insertCompany(id, name, description)
        if (name is not None):
            company.name = name
        if (description is not None):
            company.description = description
        try:
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def companyInfo(id):
        company = Company.query.filter_by(company_id=id).first()
        print(id)
        if (company is None):
            raise Exception('Nonexistent')
        return {'company_id': company.company_id, 'name': company.name,
                'description': company.description}

    @staticmethod
    def companyID(companyName):
        company = Company.query.filter_by(name=companyName).first()
        if (company is None):
            raise Exception('Nonexistent')
        return company.company_id