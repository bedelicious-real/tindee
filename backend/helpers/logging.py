import pprint

class Logging:
    pp = pprint.PrettyPrinter(indent=4)

    @staticmethod
    def print(data):
        Logging.pp.pprint(data)