from api.sensors import get_water_measurement
from api.model import Water
from api.persistence import connect
from datetime import datetime


def measure_and_persist_water(timestamp):
    distance, height, is_running = get_water_measurement()
    water = Water(height_mm=height, distance_to_water_mm=distance,
                  pump_working=is_running, sample_date=timestamp)
    session = connect()
    session.add(water)
    session.commit()


if __name__ == '__main__':
    now = datetime.now()
    measure_and_persist_water(now)
