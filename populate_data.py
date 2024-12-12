from backend.models.database import db, WaterQuality, Meteorological
from datetime import datetime
from factory import create_app

app = create_app()

# Sample data for population
water_quality_data = [
    {"parameter": "pH", "value": 7.2, "timestamp": datetime(2023, 12, 10, 8, 0)},
    {"parameter": "Dissolved Oxygen", "value": 8.1, "timestamp": datetime(2023, 12, 10, 9, 0)},
    {"parameter": "Turbidity", "value": 5.2, "timestamp": datetime(2023, 12, 10, 10, 0)},
]

meteorological_data = [
    {"parameter": "Temperature", "value": 27.5, "timestamp": datetime(2023, 12, 10, 8, 0)},
    {"parameter": "Humidity", "value": 82.4, "timestamp": datetime(2023, 12, 10, 9, 0)},
    {"parameter": "Wind Speed", "value": 5.6, "timestamp": datetime(2023, 12, 10, 10, 0)},
]

def populate_data():
    with app.app_context():
        # Add water quality data
        for entry in water_quality_data:
            new_entry = WaterQuality(
                parameter=entry["parameter"],
                value=entry["value"],
                timestamp=entry["timestamp"]
            )
            db.session.add(new_entry)

        # Add meteorological data
        for entry in meteorological_data:
            new_entry = Meteorological(
                parameter=entry["parameter"],
                value=entry["value"],
                timestamp=entry["timestamp"]
            )
            db.session.add(new_entry)

        db.session.commit()
        print("Data successfully populated.")

if __name__ == "__main__":
    populate_data()
