from api.model import Climate, Soil, Water
from datetime import datetime


class TestClimate(object):
    def test_id(self):
        climate = Climate()
        assert None is climate.id
        climate = Climate(id=3)
        assert 3 == climate.id

    def test_sample_date(self):
        timestamp = datetime.now()
        climate = Climate(sample_date=timestamp)
        assert timestamp == climate.sample_date


class TestSoil(object):
    def test_id(self):
        soil = Soil()
        assert None is soil.id
        soil = Soil(id=2)
        assert 2 == soil.id

    def test_sample_date(self):
        timestamp = datetime.now()
        soil = Soil(sample_date=timestamp)
        assert timestamp == soil.sample_date


class TestWater(object):
    def test_id(self):
        water = Water(id=1)
        assert 1 == water.id

    def test_sample_date(self):
        timestamp = datetime.now()
        water = Soil(sample_date=timestamp)
        assert timestamp == water.sample_date
