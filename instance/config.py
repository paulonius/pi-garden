# /instance/config.py

import os
from configparser import ConfigParser


class Config(object):
    """
    Parent configuration class.
    """
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')


class DevelopmentConfig(Config):
    """
    Configuration for development.
    """
    DEBUG = True


class TestingConfig(Config):
    """
    Configuration for testing, with a separate test database.
    """
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://garden@localhost/test_db'
    DEBUG = True


class StagingConfig(Config):
    """
    Configuration for Staging.
    """
    DEBUG = True


class ProductionConfig(Config):
    """
    Configuration for Production.
    """
    DEBUG = False
    TESTING = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}


config_ini = ConfigParser()
dirname = os.path.dirname(__file__)
config_ini.read(os.path.join(dirname, '../config.ini'))
