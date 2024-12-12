from flask import Flask
from backend.models.database import db
from backend.alerts import get_alerts
from backend.history import get_history
from backend.inject_data import inject_data
from backend.routes import bp 

def create_app():
    app = Flask(__name__)
    

    # Database configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///water_monitoring.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(app)

    # Define routes
    app.register_blueprint(bp)
    @app.route('/')
    def index():
        return "Water Monitoring Backend is running!"

    @app.route('/api/parameters', methods=['GET'])
    def get_parameters():
        from models.database import WaterQuality, Meteorological
        water_data = WaterQuality.query.order_by(WaterQuality.timestamp.desc()).all()
        meteorological_data = Meteorological.query.order_by(Meteorological.timestamp.desc()).all()

        water_quality = [
            {"id": w.id, "parameter": w.parameter, "value": w.value, "timestamp": w.timestamp}
            for w in water_data
        ]
        meteorological = [
            {"id": m.id, "parameter": m.parameter, "value": m.value, "timestamp": m.timestamp}
            for m in meteorological_data
        ]

        return {
            "water_quality": water_quality,
            "meteorological": meteorological
        }

    @app.route('/api/parameters', methods=['POST'])
    def add_parameter():
        from flask import request
        from models.database import WaterQuality, Meteorological
        from datetime import datetime
        data = request.get_json()
        parameter_type = data.get("type")  # "water" or "meteorological"
        parameter = data.get("parameter")
        value = data.get("value")
        timestamp = datetime.utcnow()

        if parameter_type == "water":
            new_entry = WaterQuality(parameter=parameter, value=value, timestamp=timestamp)
        elif parameter_type == "meteorological":
            new_entry = Meteorological(parameter=parameter, value=value, timestamp=timestamp)
        else:
            return {"error": "Invalid parameter type"}, 400

        db.session.add(new_entry)
        db.session.commit()
        return {"message": "Data added successfully!"}, 201

    @app.route('/api/thresholds', methods=['GET'])
    def get_thresholds():
        from models.database import Threshold
        thresholds = Threshold.query.all()
        data = [
            {
                "parameter": t.parameter,
                "lower_threshold": t.lower_threshold,
                "upper_threshold": t.upper_threshold
            }
            for t in thresholds
        ]
        return data

    @app.route('/api/alerts', methods=['GET'])
    def alerts():
        return get_alerts()

    @app.route('/api/history', methods=['GET'])
    def history():
        return get_history()

    @app.route('/api/inject-data', methods=['POST'])
    def inject_data_endpoint():
        return inject_data()

    return app
