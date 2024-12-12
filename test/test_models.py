# tests/test_models.py

from backend.models.database import db, WaterQuality, Meteorological  # Import your models
import pytest

def test_water_quality_model(client, setup_db):
    wq = WaterQuality(parameter="Temperature", value=22.5)
    db.session.add(wq)
    db.session.commit()
    
    retrieved = WaterQuality.query.get(wq.id)
    assert retrieved.parameter == "Temperature"
    assert retrieved.value == 22.5

def test_meteorological_model(client, setup_db):
    met = Meteorological(parameter="Humidity", value=75.0)
    db.session.add(met)
    db.session.commit()
    
    retrieved = Meteorological.query.get(met.id)
    assert retrieved.parameter == "Humidity"
    assert retrieved.value == 75.0

