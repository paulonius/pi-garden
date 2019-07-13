from batch.sonar import ranger
from batch.pump import pump
import pigpio


def get_pump_state():
    pi = pigpio.pi()
    is_running = pump(pi).is_running()
    pi.close()
    return is_running


def get_water_measurement():
    pi = pigpio.pi()
    distance_mm, water_level = ranger(pi).read_both()
    is_running = pump(pi).is_running()
    pi.close()
    return distance_mm, water_level, is_running
