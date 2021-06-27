from flask import request
from flask_restful import Resource, Api, marshal_with, reqparse
from flask_restful_swagger import swagger
import flask_minimal.fundamental_indicators_provider as fundamental_indicators_provider
from .models import FundamentalAnalysisResult
from .errors import MissingStockError
import time

class FAEndpoint(Resource):
    @swagger.operation(
        responseClass=FundamentalAnalysisResult.__name__,
        nickname='fa',
        parameters=[
            {
                "name": "name",
                "description": "JSON-encoded name",
                "required": True,
                "allowMultiple": False,
                "dataType": "string",
                "paramType": "body"
            },
        ])
    @marshal_with(FundamentalAnalysisResult.resource_fields)
    def get(self):
        """Return a FundamentalAnalysisResult object

        Lightweight response to let us confirm that the server is on-line"""
        parser = reqparse.RequestParser()
        parser.add_argument('stock', type=str)
        args =  parser.parse_args()
        stock = args['stock']
        if stock:
            company = fundamental_indicators_provider.Company(stock)
            fundamental_indicators_provider.get_fundamental_indicators_for_company({}, company)
            return FundamentalAnalysisResult(company.fundamental_indicators)
        else:
            return MissingStockError()
