from flask import current_app
from backend.models.database import db, WaterQuality, Meteorological
from datetime import datetime

def inject_data():
    with current_app.app_context():  # Use the current Flask application context
        # Add sample data to the database
        water_data = [
            {"parameter": "pH", "value": 7.5, "timestamp": datetime.utcnow()},
            {"parameter": "Dissolved Oxygen", "value": 8.0, "timestamp": datetime.utcnow()},
        ]

        meteorological_data = [
            {"parameter": "Temperature", "value": 25.0, "timestamp": datetime.utcnow()},
            {"parameter": "Humidity", "value": 65.0, "timestamp": datetime.utcnow()},
        ]

        # Add water quality data
        for data in water_data:
            new_entry = WaterQuality(**data)
            db.session.add(new_entry)

        # Add meteorological data
        for data in meteorological_data:
            new_entry = Meteorological(**data)
            db.session.add(new_entry)

        db.session.commit()

    return {"message": "Sample data injected successfully!"}

