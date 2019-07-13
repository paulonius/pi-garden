from batch.sonar import ranger
from batch.pump import pump as pump
from api.persistence import config
import pigpio


def create_sonar(pi):
    return ranger(pi, config['SENSORS']['SonarTrigger'],
                  config['SENSORS']['SonarEcho'])


def create_pump(pi):
    return pump(pi, config['SENSORS']['Pump'])


def get_pump_state():
    pi = pigpio.pi()
    is_running = create_pump(pi).is_running()
    pi.close()
    return is_running


def get_water_measurement():
    pi = pigpio.pi()
    distance_mm, water_level = create_sonar(pi).read_both()
    is_running = create_pump(pi).is_running()
    pi.close()
    return distance_mm, water_level, is_running
