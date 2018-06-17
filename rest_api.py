from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


@api.resource('/user')
class CreateUser(Resource):
    def post(self):
        return {'status': 'success'}


@api.resource('/news/<string:category>')  # TODO add
class NaverNews(Resource):
    def get(self):
        return {}

class NaverNewsSearch(Resource):
    def post(self):
        pass


def run_api_server(**kwargs):
    app.run(kwargs)
