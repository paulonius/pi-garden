from api.persistence import config, db_uri
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
