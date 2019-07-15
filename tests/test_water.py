# test_water.py
import pytest
import json
from api import create_app, db
from datetime import datetime


@pytest.fixture
def water():
    return {
        'sample_date': datetime(2001, 8, 5),
        'height_mm': 205.54,
        'distance_to_water_mm': 695.01,
        'pump_working': False
    }


@pytest.fixture
def client():
    app = create_app(config_name='testing')
    client = app.test_client
    with app.app_context():
        db.create_all()

    yield client

    with app.app_context():
        db.session.remove()
        db.drop_all()


class TestWater(object):
    def test_water_creation(self, water, client):
        res = client.post('/water/', data=water)
        assert 201 == res.status_code
        assert '205.54' in str(res.data)

    def test_api_can_get_last_100_water(self, water, client):
        res = client.post('/water/', data=water)
        assert 201 == res.status_code
        res = client.get('/water/')
        assert 200 == res.status_code
        assert '205.54' in str(res.data)

    def test_api_can_get_water_by_id(self, water, client):
        rv = client.post('/water/', data=water)
        assert 201 == rv.status_code
        result_in_json = json.loads(rv.data.decode('utf-8').replace("'", "\""))
        result = client.get('/water/{}'.format(result_in_json['id']))
        assert 200 == result.status_code
        assert '205.54' in str(result.data)

    def test_water_can_be_edited(self, water, client):
        rv = client.post('/water/', data={'height_mm': 299.12})
        assert 200 == rv.status_code
        rv = client.put('/water/1', data=water)
        assert 200 == rv.status_code
        result = client.get('/water/1')
        assert '205.54' in str(result.data)

    def test_water_deletion(self, water, client):
        rv = client.post('/water/', data=water)
        assert 201 == rv.status_code
        res = self.client.delete('/water/1')
        assert 200 == res.status_code
        # Test to see if it exists, should return a 404
        result = client.get('/water/1')
        assert 404 == result.status_code
