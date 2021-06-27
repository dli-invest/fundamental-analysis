from flask import Flask, request
from flask_restful import Resource, Api, marshal_with, fields, abort
from flask_restful_swagger import swagger
from flask_minimal.api import DummyEndpoint
from flask_minimal.api import HelloEndpoint
from flask_minimal.api import FAEndpoint

API_VERSION_NUMBER = '1.0'
API_VERSION_LABEL = 'v1'


class CustomFlaskApp(object):

    def __init__(self):
        self.app = Flask(__name__)
        custom_errors = {
            'JsonInvalidError': {
                'status': 500,
                'message': 'JSON format not valid'
            },
            'JsonRequiredError': {
                'status': 400,
                'message': 'JSON input required'
            }
        }
        self.api = swagger.docs(Api(self.app, errors=custom_errors), apiVersion=API_VERSION_NUMBER)
        
        self.api.add_resource(DummyEndpoint, '/dummy', endpoint='dummy')
        self.api.add_resource(HelloEndpoint, '/hello', endpoint='hello')
        self.api.add_resource(FAEndpoint, '/fa', endpoint='fa')

    def run(self, *args, **kwargs):
        self.app.config['PROPAGATE_EXCEPTIONS'] = False
        self.app.run(*args, **kwargs)


def run_app(*args, **kwargs):
    app = CustomFlaskApp()
    app.run(*args, **kwargs)

def heroku_run_app():
    run_app(debug=True, port=8080)

if __name__ == '__main__':
    run_app(debug=True, port=8080)