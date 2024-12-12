from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Water Quality Parameter Model
class WaterQuality(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    parameter = db.Column(db.String(50), nullable=False)
    value = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)

# Meteorological Parameter Model
class Meteorological(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    parameter = db.Column(db.String(50), nullable=False)
    value = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)

# Threshold Model
class Threshold(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    parameter = db.Column(db.String(50), nullable=False, unique=True)
    lower_threshold = db.Column(db.Float, nullable=False)
    upper_threshold = db.Column(db.Float, nullable=False)
from flask_sqlalchemy import SQLAlchemy

class History(db.Model):
    __tablename__ = 'history'
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, nullable=False)
    parameter = db.Column(db.String(50), nullable=False)
    value = db.Column(db.Float, nullable=False)


