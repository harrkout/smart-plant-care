from .. import db
from ..user.models import User
from sqlalchemy import PrimaryKeyConstraint, ForeignKeyConstraint, UniqueConstraint
#from werkzeug.security import generate_password_hash, check_password_hash
#from .. import login
#from flask_login import UserMixin
#from ..models import Todo

#from SmartPlantCare import db
from datetime import datetime

class Sensor(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    loc_longtitute = db.Column(db.Float, nullable=False)
    loc_latitude = db.Column(db.Float, nullable=False)
    crop_id = db.Column(db.Integer, db.ForeignKey('crop.id'), nullable=False)

    def __repr__(self):
        return f"{self.id}:{self.crop_id}:{self.loc_longtitute}:{self.loc_latitude}"

class SensorData(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date_time = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    velue = db.Column(db.Float, nullable=False)
    sensor_id = db.Column(db.Integer, db.ForeignKey('sensor.id'), nullable=False)

    def __repr__(self):
        return f"{self.id}:{self.sensor_id}"