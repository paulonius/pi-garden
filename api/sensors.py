from batch.sonar import ranger
from batch.configloader import config
import pigpio


def get_water_distance():
    pi = pigpio.pi()
    sonar = ranger(pi, config['SENSORS']['SonarTrigger'],
                   config['SENSORS']['SonarEcho'])
    distance_mm = sonar.read_mm()
    pi.close()
    return distance_mm


def get_water_level():
    pi = pigpio.pi()
    sonar = ranger(pi, config['SENSORS']['SonarTrigger'],
                   config['SENSORS']['SonarEcho'])
    height_mm = sonar.read_water_level()
    pi.close()
    return height_mm
