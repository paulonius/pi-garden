import pigpio
import batch.sonar

from api.sensors import get_water_distance, get_water_level
from api.persistence import config


class TestDistance(object):
    def test_config_has_pins_and_height(self):
        assert None is not config['SENSORS']['SonarTrigger']
        assert None is not config['SENSORS']['SonarEcho']
        assert None is not config['SENSORS']['SonarHeight']

    def test_get_distance_exists(self):
        assert None is not get_water_distance

    def test_get_distance_inits_pi(self, mocker):
        pi = mocker.patch('pigpio.pi')
        get_water_distance()
        pi.assert_called_once()

    def test_get_distance_reads_mm(self, mocker):
        mocker.patch('pigpio.pi')
        ranger = mocker.patch('batch.sonar.ranger.read_mm')
        get_water_distance()
        ranger.assert_called_once()

    def test_get_distance_returns_mm(self, mocker):
        mocker.patch('pigpio.pi')
        ranger = mocker.patch('batch.sonar.ranger.read_mm')
        ranger.return_value = 332.32
        dist = get_water_distance()
        assert 332.32 == dist

    def test_get_water_level_exists(self):
        assert None is not get_water_level

    def test_get_water_level_inits_pi(self, mocker):
        pi = mocker.patch('pigpio.pi')
        get_water_level()
        pi.assert_called_once()

    def test_get_water_level_calls_get_water_distance(self, mocker):
        mocker.patch('pigpio.pi')
        distancer = mocker.patch('batch.sonar.ranger.read_water_level')
        get_water_level()
        distancer.assert_called_once()

    def test_get_water_level_returns_distance(self, mocker):
        mocker.patch('pigpio.pi')
        distancer = mocker.patch('batch.sonar.ranger.read_water_level')
        distancer.return_value = 332.32
        water_level = get_water_level()
        assert isinstance(water_level, float)

    def test_get_water_level_returns_meaningful_value(self, mocker):
        mocker.patch('pigpio.pi')
        distancer = mocker.patch('batch.sonar.ranger.read_water_level')
        height = float(config['SENSORS']['SonarHeight'])
        distancer.return_value = height - 332.32
        water_level = get_water_level()
        assert 332.32 != water_level
        assert 0.0 < water_level and height > water_level
