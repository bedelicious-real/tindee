from sqlite3 import IntegrityError
from sqlalchemy import ForeignKey, false
from database.db import TindeeUser, Mentor, Mentee
from . import db as db_file
from sqlalchemy.orm import backref as bf

db = db_file.db

# Job of Mentor


class Job(db.Model):
    __tablename__ = 'job'
    email = db.Column(db.String(50), ForeignKey(
        'tindeeUser.email'), primary_key=True, nullable=False)
    job_name = db.Column(db.String(100), primary_key=True, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    annual_salary = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(1000), nullable=False)

    user = db.relationship('TindeeUser', backref=bf(
        'job', uselist=False), foreign_keys='[job.email]')

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
    company_id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(1000), nullable=False)

    def __init__(self, company_id, name, description):
        self.company_id = company_id
        self.name = name
        self.description = description

    @staticmethod
    def insertCompany(company_id, name, description):
        newCompany = Company(company_id, name, description)
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
        company = Company.query.filter_by(company_id=id)
        if (company is None):
            raise Exception('Nonexistent')
        return {'company_id': company.company_id, 'name': company.name,
                'description': company.description}
