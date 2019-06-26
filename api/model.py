from sqlalchemy import Column, Integer, DateTime, Numeric, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Climate(Base):
    __tablename__ = 'climate'

    id = Column(Integer, primary_key=True)
    sample_date = Column(DateTime)
    temperature = Column(Numeric(precision=3, scale=1))
    humidity_percent = Column(Numeric(precision=3, scale=1))
    external_temperature = Column(Numeric(precision=3, scale=1))
    external_humidity_percent = Column(Numeric(precision=3, scale=1))

    def __repr__(self):
        repr = ("<Climate(id='{}', sample_date='{}', temperature='{}', "
                "humidityPercent='{}', externalTemperature='{}', "
                "externalHumidityPercent='{}')>")
        return repr.format(self.id, self.sample_date, self.temperature,
                           self.humidity_percent, self.external_temperature,
                           self.external_humidity_percent)


class Soil(Base):
    __tablename__ = 'soil'

    id = Column(Integer, primary_key=True)
    sample_date = Column(DateTime)
    probe = Column(Integer)
    moisture_percent = Column(Numeric(precision=3, scale=1))
    conductivity = Column(Numeric(precision=6, scale=2))

    def __repr__(self):
        repr = ("<Soil(id='{}', sample_date='{}', probe='{}', "
                "moisture_percent='{}', conductivity='{}')>")
        return repr.format(self.id, self.sample_date, self.probe,
                           self.moisture_percent, self.conductivity)


class Water(Base):
    __tablename__ = 'water'

    id = Column(Integer, primary_key=True)
    sample_date = Column(DateTime)
    height_mm = Column(Integer)
    distance_to_water_mm = Column(Integer)
    pump_working = Column(Boolean)

    def __repr__(self):
        repr = ("<Water(id='{}', sample_date='{}', height_mm='{}', "
                "distance_to_water_mm='{}', pump_working='{}')>")
        return repr.format(self.id, self.sample_date, self.height_mm,
                           self.distance_to_water_mm, self.pump_working)
