from flask import jsonify, request
from backend.models.database import db, WaterQuality, Meteorological
from datetime import datetime

def get_history():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    
    # Fetch data within the date range
    query = db.session.query(WaterQuality, Meteorological).filter(
        (WaterQuality.timestamp >= start_date) & (WaterQuality.timestamp <= end_date) if start_date and end_date else True
    ).all()

    data = {
        "water_quality": [
            {
                "id": w.id,
                "parameter": w.parameter,
                "value": w.value,
                "timestamp": w.timestamp
            } for w in query[0]
        ],
        "meteorological": [
            {
                "id": m.id,
                "parameter": m.parameter,
                "value": m.value,
                "timestamp": m.timestamp
            } for m in query[1]
        ]
    }

    return jsonify(data)
