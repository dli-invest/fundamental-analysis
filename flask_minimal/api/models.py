from flask_restful import Resource, Api, marshal_with, fields, abort
from flask_restful_swagger import swagger

@swagger.model
class DummyResult(object):
    """The result of a call to /dummy"""
    resource_fields = {
        'dummy': fields.String
    }

    def __init__(self):
        self.dummy = "foobar"


@swagger.model
class HelloResult(object):
    """The result of a call to /hello"""
    resource_fields = {
        'greetings': fields.String
    }

    def __init__(self, name):
        self.greetings = "Hello {}".format(name)

@swagger.model
class FundamentalAnalysisResult(object):
    """The result of a call to /fa"""
    resource_fields = {
        'MarketCap': fields.String,
        'PS': fields.String,
        'PE': fields.String,
        'PEG': fields.String,
        'ProfitMargin': fields.String,
        'OperMargin': fields.String,
        'CurrentRatio': fields.String,
        'DivPayoutRatio': fields.String,
        'ROA': fields.Float,
        'ROE': fields.Float,
        'Cash/Share': fields.Float,
        'Book/Share': fields.Float,
        'Debt/Equity': fields.Float
    }

    def __init__(self, data):
        self.__dict__.update(data)