from urllib.request import urlopen
from api.persistence import config
import json

# https://www.meteogalicia.gal/datosred/infoweb/meteo/docs/rss/JSON_ultimos10min_gl.pdf
climateUrl = config['URLS']['ClimateUrl']


def getLocalClimate():
    req = urlopen(climateUrl)
    humidity, temperature = '', ''
    if (req.getcode() == 200):
        result = json.loads(req.read())
        for measurement in result['listUltimos10min'][0]['listaMedidas']:
            if (measurement['codigoParametro'] == 'HR_AVG_1.5m'):
                humidity = measurement['valor']
            elif (measurement['codigoParametro'] == 'TA_AVG_1.5m'):
                temperature = measurement['valor']
    return temperature, humidity
