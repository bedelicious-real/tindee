from database.db import Mentor, TindeeUser

class Search():
    searcher = None

    def __init__(self):
        self.searcher = Mentor.query.join(TindeeUser)

    def search_by_first_name(self, firstName):
        if (firstName is not None):
            self.searcher = self.searcher.filter_by(first_name = firstName)
        return self

    def search_by_last_name(self, lastName):
        if (lastName is not None):
            self.searcher = self.searcher.filter_by(last_name = lastName)

    def search_by_offers(self, expected_offers):
        if (expected_offers is not None and expected_offers):
            self.searcher = self.searcher.filter(
                Mentor.offers.contains(expected_offers))
        return self

    def search_by_concentrations(self, expected_concentrations):
        if (expected_concentrations is not None and expected_concentrations):
            self.searcher = self.searcher.filter(
                Mentor.concentration.contains(expected_concentrations))
        return self

    def result(self):
        result = []
        mentors = self.searcher.all()
        for mentor in mentors:
            result.append({'email': mentor.email, 'first_name': mentor.user.first_name, 'last_name': mentor.user.last_name,
                'image_url': mentor.user.image_url, 'exp_years': mentor.exp_years,
                'offers': mentor.offers, 'concentration': mentor.concentration,
                'company_id': mentor.company_id})
        return result