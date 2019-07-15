from api.sensors import get_water_measurement, get_pump_state
from instance.config import config_ini


class TestDistance(object):
    def test_config_has_pins_and_height(self):
        assert None is not config_ini['SENSORS']['SonarTrigger']
        assert None is not config_ini['SENSORS']['SonarEcho']
        assert None is not config_ini['SENSORS']['SonarHeight']

    def test_get_water_measurement_exists(self):
        assert None is not get_water_measurement

    def test_get_water_measurement_inits_pi(self, mocker):
        pi = mocker.patch('pigpio.pi')
        get_water_measurement()
        pi.assert_called_once()

    def test_get_water_measurement_calls_read_both(self, mocker):
        mocker.patch('pigpio.pi')
        distancer = mocker.patch('batch.sonar.ranger.read_both')
        distancer.return_value = 0, 0
        get_water_measurement()
        distancer.assert_called_once()

    def test_get_water_measurement_returns_distance(self, mocker):
        mocker.patch('pigpio.pi')
        distancer = mocker.patch('batch.sonar.ranger.read_both')
        distancer.return_value = 332.32, 630.32
        distance, water_level, is_running = get_water_measurement()
        assert isinstance(water_level, float)

    def test_get_water_measurement_returns_meaningful_values(self, mocker):
        mocker.patch('pigpio.pi')
        distancer = mocker.patch('batch.sonar.ranger.read_both')
        height = float(config_ini['SENSORS']['SonarHeight'])
        distancer.return_value = 332.32, height - 332.32
        pump = mocker.patch('batch.pump.pump.is_running')
        pump.return_value = True
        distance, water_level, is_running = get_water_measurement()
        assert 332.32 != water_level
        assert 332.32 == distance
        assert 0.0 < water_level and height > water_level
        assert True is is_running


class TestPump(object):
    def get_pump_state_should_exist(self):
        assert None is not get_pump_state

    def test_get_pump_state_inits_pi(self, mocker):
        pi = mocker.patch('pigpio.pi')
        get_pump_state()
        pi.assert_called_once()

    def test_get_pump_state_should_return_boolean(self, mocker):
        mocker.patch('pigpio.pi')
        pump = mocker.patch('batch.pump.pump.is_running')
        pump.return_value = True
        assert True is get_pump_state()
