from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from batch.configloader import config


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
