import configparser
import os

dirname = os.path.dirname(__file__)
if "pi-garden" in dirname:
    config_file = os.path.join(dirname, '../config.ini')
else:
    config_file = os.path.join(os.environ['HOME'], 'pi-garden/config.ini')

config = configparser.ConfigParser()
config.read(config_file)
