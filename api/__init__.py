# app/__init__.py

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from instance.config import app_config

# initialize sql-achemy
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    from api.resources.water import Water, WaterCollection
    api = Api(app)
    api.add_resource(WaterCollection, '/water')
    api.add_resource(Water, '/water/<int:id>')
    return app
