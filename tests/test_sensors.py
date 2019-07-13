from api.sensors import get_water_distance
import pigpio


class TestDistance(object):
    def test_get_distance_exists(self):
        assert None is not get_water_distance
