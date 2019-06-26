from batch.climate import getDHTdata
from api.model import Climate


class TestGetDHTData(object):
    def test_function_exists(self):
        assert None is not getDHTdata

    def test_function_returns_climate(self):
        assert isinstance(getDHTdata(), Climate)
