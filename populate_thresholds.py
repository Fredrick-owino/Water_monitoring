from app import app
from backend.models.database import db, Threshold

# Threshold values
thresholds = [
    {"parameter": "Dissolved Oxygen (DO)", "lower_threshold": 4.0, "upper_threshold": 10.0},
    {"parameter": "pH", "lower_threshold": 6.0, "upper_threshold": 9.0},
    {"parameter": "Water Temperature", "lower_threshold": 20.0, "upper_threshold": 35.0},
    {"parameter": "Turbidity", "lower_threshold": 0, "upper_threshold": 20.0},
    {"parameter": "Ammonia", "lower_threshold": 0.0, "upper_threshold": 0.1},
    {"parameter": "Nitrate", "lower_threshold": 0, "upper_threshold": 50.0},
    {"parameter": "Total Dissolved Solids (TDS)", "lower_threshold": 50.0, "upper_threshold": 1000.0},
    {"parameter": "Salinity", "lower_threshold": 0, "upper_threshold": 5.0},
    {"parameter": "Air Temperature", "lower_threshold": 20.0, "upper_threshold": 35.0},
    {"parameter": "Relative Humidity", "lower_threshold": 40.0, "upper_threshold": 90.0},
    {"parameter": "Rainfall", "lower_threshold": 1.0, "upper_threshold": 50.0},
    {"parameter": "Wind Speed", "lower_threshold": 0.5, "upper_threshold": 10.0},
    {"parameter": "Solar Radiation", "lower_threshold": 200.0, "upper_threshold": 1200.0},
    {"parameter": "Atmospheric Pressure", "lower_threshold": 980.0, "upper_threshold": 1030.0},
]

with app.app_context():
    for item in thresholds:
        threshold = Threshold(**item)
        db.session.add(threshold)
    db.session.commit()
    print("Threshold data populated successfully.")
