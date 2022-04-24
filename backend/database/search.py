from . import db as db_file
from database.db import Mentor
from sqlalchemy.orm import backref as bf

db = db_file.db


class Search(db.Model):
    __tablename__ = 'search'
    searcher = None

    def __init__(self):
        self.searcher = Mentor.query

    def search_by_first_name(self, firstName):
        if (firstName is not None):
            self.searcher = self.searcher.filter_by(first_name=firstName)
        return self

    def search_by_last_name(self, lastName):
        if (lastName is not None):
            self.searcher = self.searcher.filter_by(last_name=lastName)

    def search_by_offers(self, expected_offers):
        if (expected_offers is not None and expected_offers):
            self.searcher = self.searcher.filter_by(
                Mentor.offers.contains(expected_offers))
        return self

    def search_by_concentrations(self, expected_concentrations):
        if (expected_concentrations is not None and expected_concentrations):
            self.searcher = self.searcher.filter_by(
                Mentor.concentration.contains(expected_concentrations))
        return self

    def result(self):
        return self.searcher.all()
