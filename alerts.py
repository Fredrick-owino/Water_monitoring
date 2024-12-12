from flask import jsonify
from backend.models.database import db, WaterQuality, Meteorological, Threshold
from datetime import datetime

def get_alerts():
    # Fetch all data from water_quality and meteorological tables
    water_data = WaterQuality.query.all()
    meteorological_data = Meteorological.query.all()

    # Fetch all thresholds
    thresholds = {t.parameter: (t.lower_threshold, t.upper_threshold) for t in Threshold.query.all()}

    # Initialize alerts list
    alerts = []

    # Check water quality data against thresholds
    for w in water_data:
        lower, upper = thresholds.get(w.parameter, (None, None))
        if lower is not None and (w.value < lower or w.value > upper):
            alerts.append({
                "parameter": w.parameter,
                "value": w.value,
                "timestamp": w.timestamp,
                "breach_time": datetime.utcnow().isoformat()
            })

    # Check meteorological data against thresholds
    for m in meteorological_data:
        lower, upper = thresholds.get(m.parameter, (None, None))
        if lower is not None and (m.value < lower or m.value > upper):
            alerts.append({
                "parameter": m.parameter,
                "value": m.value,
                "timestamp": m.timestamp,
                "breach_time": datetime.utcnow().isoformat()
            })

    return jsonify(alerts)
