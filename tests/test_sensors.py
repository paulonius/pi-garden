from api.sensors import getDHTdata
import Adafruit_DHT


class TestGetDHTData(object):
    def test_function_exists(self):
        assert None is not getDHTdata

    def test_dht_returns_data(self, mocker):
        reader = mocker.patch.object(Adafruit_DHT, 'read_retry')
        reader.return_value = 33.42, 15.42
        temp, humid = getDHTdata()
        assert 15.42 == temp
        assert 33.42 == humid
