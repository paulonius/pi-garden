from api import db


class Climate(db.Model):
    __tablename__ = 'climate'

    id = db.Column(db.Integer, primary_key=True)
    sample_date = db.Column(db.DateTime)
    temperature = db.Column(db.Numeric(precision=3, scale=1))
    humidity_percent = db.Column(db.Numeric(precision=3, scale=1))
    external_temperature = db.Column(db.Numeric(precision=3, scale=1))
    external_humidity_percent = db.Column(db.Numeric(precision=3, scale=1))

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        repr = ("<Climate(id='{}', sample_date='{}', temperature='{}', "
                "humidityPercent='{}', externalTemperature='{}', "
                "externalHumidityPercent='{}')>")
        return repr.format(self.id, self.sample_date, self.temperature,
                           self.humidity_percent, self.external_temperature,
                           self.external_humidity_percent)


class Soil(db.Model):
    __tablename__ = 'soil'

    id = db.Column(db.Integer, primary_key=True)
    sample_date = db.Column(db.DateTime)
    probe = db.Column(db.Integer)
    moisture_percent = db.Column(db.Numeric(precision=3, scale=1))
    conductivity = db.Column(db.Numeric(precision=6, scale=2))

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        repr = ("<Soil(id='{}', sample_date='{}', probe='{}', "
                "moisture_percent='{}', conductivity='{}')>")
        return repr.format(self.id, self.sample_date, self.probe,
                           self.moisture_percent, self.conductivity)


class Water(db.Model):
    __tablename__ = 'water'

    id = db.Column(db.Integer, primary_key=True)
    sample_date = db.Column(db.DateTime)
    height_mm = db.Column(db.Integer)
    distance_to_water_mm = db.Column(db.Integer)
    pump_working = db.Column(db.Boolean)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        repr = ("<Water(id='{}', sample_date='{}', height_mm='{}', "
                "distance_to_water_mm='{}', pump_working='{}')>")
        return repr.format(self.id, self.sample_date, self.height_mm,
                           self.distance_to_water_mm, self.pump_working)
