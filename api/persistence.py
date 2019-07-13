from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import configparser
import os

dirname = os.path.dirname(__file__)
if "pi-garden" in dirname:
    config_file = os.path.join(dirname, '../config.ini')
else:
    config_file = os.path.join(os.environ['HOME'], 'pi-garden/config.ini')

config = configparser.ConfigParser()
config.read(config_file)

db_uri = "{}//{}:{}@{}:{}/{}"
db_uri = db_uri.format(config['DATABASE']['Protocol'],
                       config['DATABASE']['User'],
                       config['DATABASE']['Password'],
                       config['DATABASE']['Host'], config['DATABASE']['Port'],
                       config['DATABASE']['Database'])

engine = create_engine(db_uri, client_encoding='utf8')
Session = sessionmaker(bind=engine)


def connect():
    return Session()
