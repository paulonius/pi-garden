from api.persistence import config, db_uri, connect, engine
from api.model import Water
from sqlalchemy import desc
import re


class TestConfig(object):
    def test_exists(self):
        assert None is not config

    def test_database(self):
        assert None is not config['DATABASE']

    def test_needed_params(self):
        assert len(config['DATABASE']['Protocol']) > 0
        assert len(config['DATABASE']['Database']) > 0
        assert len(config['DATABASE']['Host']) > 0
        assert len(config['DATABASE']['Port']) == 4
        assert len(config['DATABASE']['User']) > 0
        assert len(config['DATABASE']['Password']) > 0


class TestDbUri(object):
    def test_db_uri_exists(self):
        assert None is not db_uri

    def test_db_uri_follows_format(self):
        assert re.match("^[a-z]+://.+:.+@.+/.+$", db_uri)


class TestConnect(object):
    def test_connect_objects(self):
        session = connect()
        assert engine is not None
        assert session is not None

    def test_session(self):
        session = connect()
        water = Water(height_mm=23)
        session.add(water)
        db_water = session.query(Water).filter_by(height_mm='23').order_by(
            desc(Water.id)).first()
        assert db_water is water
        session.rollback()
