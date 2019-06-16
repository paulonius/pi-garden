import configparser
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

config = configparser.ConfigParser()
config.read('config.ini')

dbUri = "{}//{}:{}@{}/{}".format(config['DATABASE']['Protocol'],
                                 config['DATABASE']['User'],
                                 config['DATABASE']['Password'],
                                 config['DATABASE']['Host'],
                                 config['DATABASE']['Database'])

engine = create_engine(dbUri)
Session = sessionmaker(bind=engine)
