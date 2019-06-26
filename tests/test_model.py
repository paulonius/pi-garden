from api.model import Climate, Soil, Water
from datetime import datetime


class TestClimate(object):
    def test_id(self):
        climate = Climate()
        assert None is climate.id
        climate = Climate(id=3)
        assert 3 == climate.id

    def test_sample_date(self):
        climate = Climate()
        assert None is climate.sample_date
        timestamp = datetime.now()
        climate = Climate(sample_date=timestamp)
        assert timestamp == climate.sample_date

    def test_temperature(self):
        climate = Climate()
        assert None is climate.temperature
        assert None is climate.external_temperature
        temp = 15.32
        climate = Climate(temperature=temp, external_temperature=temp)
        assert 15.32 == climate.temperature
        assert 15.32 == climate.external_temperature

    def test_humidity(self):
        climate = Climate()
        assert None is climate.humidity_percent
        assert None is climate.external_humidity_percent
        humidity = 52
        climate = Climate(humidity_percent=humidity,
                          external_humidity_percent=humidity)
        assert 52 == climate.humidity_percent
        assert 52 == climate.external_humidity_percent


class TestSoil(object):
    def test_id(self):
        soil = Soil()
        assert None is soil.id
        soil = Soil(id=2)
        assert 2 == soil.id

    def test_sample_date(self):
        soil = Soil()
        assert None is soil.sample_date
        timestamp = datetime.now()
        soil = Soil(sample_date=timestamp)
        assert timestamp == soil.sample_date

    def test_probe(self):
        soil = Soil()
        assert None is soil.probe
        soil = Soil(probe=3)
        assert 3 == soil.probe

    def test_moisture_percent(self):
        soil = Soil()
        assert None is soil.moisture_percent
        soil = Soil(moisture_percent=15)
        assert 15 == soil.moisture_percent

    def test_conductivity(self):
        soil = Soil()
        assert None is soil.moisture_percent
        soil = Soil(conductivity=0)
        assert 0 == soil.conductivity


class TestWater(object):
    def test_id(self):
        water = Water(id=1)
        assert 1 == water.id

    def test_sample_date(self):
        water = Water()
        assert None is water.sample_date
        timestamp = datetime.now()
        water = Soil(sample_date=timestamp)
        assert timestamp == water.sample_date

    def test_height_mm(self):
        water = Water()
        assert None is water.height_mm
        water = Water(height_mm=49)
        assert 49 == water.height_mm

    def test_distance_to_water_mm(self):
        water = Water()
        assert None is water.distance_to_water_mm
        water = Water(distance_to_water_mm=92)
        assert 92 == water.distance_to_water_mm

    def test_pump_working(self):
        water = Water()
        assert None is water.pump_working
        water = Water(pump_working=False)
        assert False is water.pump_working
