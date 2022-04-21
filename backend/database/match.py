from sqlite3 import IntegrityError
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from database.db import TindeeUser, Mentor, Mentee
from . import db as db_file
from sqlalchemy.orm import backref as bf

db = db_file.db


class Like(db.Model):
    __tablename__ = 'like'
    liking_email = db.Column(db.String(50), ForeignKey(
        'tindeeUser.email'), primary_key=True, nullable=False)
    liked_email = db.Column(db.String(50), ForeignKey(
        'tindeeUser.email'), primary_key=True, nullable=False)

    # Foreign key to TindeeUser
    liking_user = db.relationship('TindeeUser', backref=bf(
        'like', uselist=False), foreign_keys='[Like.liking_email]')
    liked_user = db.relationship(
        'TindeeUser', foreign_keys='[Like.liked_email]')

    def __init__(self, liking, liked):
        self.liking_email = liking
        self.liked_email = liked

    @staticmethod
    def insertLike(liking, liked):
        newLike = Like(liking, liked)
        db.session.add(newLike)
        try:
            db.session.commit()
            return True
        except IntegrityError as integrity:
            print(integrity)
            return False
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def deleteLike(liking, liked):
        if (Like.isMatch(liking, liked)):
            Match.deleteMatch(liking, liked)
        like = Like.query.filter_by(
            liking_email=liking, liked_email=liked).first()
        db.session.delete(like)
        try:
            db.session.commit()
            return {'liking': liking, 'liked': liked}
        except Exception as e:
            print(e)
            raise Exception('Other')

    @staticmethod
    def isMatch(mentee, mentor):
        menteeLike = Like.query.filter_by(
            liking_email=mentee, liked_email=mentor).first()
        mentorLike = Like.query.filter_by(
            liking_email=mentor, liked_email=mentee).first()
        if (menteeLike is not None and mentorLike is not None):
            return True
        return False


class Match(db.Model):
    __tablename__ = 'match'
    mentor_email = db.Column(db.String(50), ForeignKey(
        'tindeeUser.email'), primary_key=True, nullable=False)
    mentee_email = db.Column(db.String(50), ForeignKey(
        'tindeeUser.email'), primary_key=True, nullable=False)

    # Foreign key to TindeeUser
    mentor_user = db.relationship('TindeeUser', backref=bf(
        'match', uselist=False), foreign_keys='[Match.mentor_email]')
    mentee_user = db.relationship(
        'TindeeUser', foreign_keys='[Match.mentee_email]')

    def __init__(self, mentor, mentee):
        self.mentor_email = mentor
        self.mentee_email = mentee

    @staticmethod
    def insertMatch(mentor, mentee):
        newMatch = Match(mentor, mentee)
        db.session.add(newMatch)
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
    def deleteMatch(mentor, mentee):
        match = Match.query.filter_by(
            mentor_email=mentor, mentee_email=mentee).first()
        if (match is None):
            match = Match.query.filter_by(
                mentor_email=mentee, mentee_email=mentor).first()
        db.session.delete(match)
        try:
            db.session.commit()
            return {'mentor': mentor, 'mentee': mentee}
        except Exception as e:
            print(e)
            raise Exception('Other')

    @staticmethod
    def getMentors(menteeEmail):
        matches = Match.query.filter_by(mentee_email=menteeEmail).all()
        return [match.mentor_email for match in matches]

    @staticmethod
    def getMentees(mentorEmail):
        matches = Match.query.filter_by(mentor_email=mentorEmail).all()
        return [match.mentee_email for match in matches]
