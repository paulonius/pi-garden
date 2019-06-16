from flask import Flask, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Employees(Resource):
    def get(self):
        return {'employees': ['Juan Marquez']}


class Tracks(Resource):
    def get(self):
        return {'data': ['123', '456']}


api.add_resource(Employees, '/employees')
api.add_resource(Tracks, '/tracks')

if __name__ == '__main__':
    app.run(port='5002')
