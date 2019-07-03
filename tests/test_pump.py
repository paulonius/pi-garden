from batch.pump import pump
import pigpio

class TestPump(object):
    def test_init_calls_pigpio(self, mocker):
        mocker.patch(pigpio)
