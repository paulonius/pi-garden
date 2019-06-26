from api.persistence import connect
from api.model import Climate
import Adafruit_DHT


def getDHTdata():
    dht_11 = Adafruit_DHT.DHT11
    return Climate()
