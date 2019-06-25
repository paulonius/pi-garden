import configparser

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

config = configparser.ConfigParser()
config.read('config.ini')

db_uri = "{}//{}:{}@{}:{}/{}"
db_uri = db_uri.format(config['DATABASE']['Protocol'],
                       config['DATABASE']['User'],
                       config['DATABASE']['Password'],
                       config['DATABASE']['Host'], config['DATABASE']['Port'],
                       config['DATABASE']['Database'])


def connect():
    con = create_engine(db_uri, client_encoding='utf8')
    meta = MetaData(bind=con, reflect=True)

    return con, meta
