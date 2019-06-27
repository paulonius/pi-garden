from api.persistence import config
import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
pin = config['SENSORS']['Dht11']


def getDHTdata():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    return temperature, humidity
