from api.external import climateUrl, getLocalClimate
import urllib.request


class TestLocalClimate(object):
    def test_url_exists(self):
        assert climateUrl is not None

    def test_get_local_climate_returns(self):
        assert getLocalClimate() is not None

    def test_get_local_climate_returns_data(self, mocker):
        temp, humid = getLocalClimate()
        assert None is not temp
        assert '' != temp
        assert None is not humid
        assert '' != humid
