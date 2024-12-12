# backend/app.py
from flask import Flask
from backend.models.database import db
from backend.routes import bp  # Ensure the import path is correct
from backend.config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    # Register blueprint
    app.register_blueprint(bp)

    return app


# Create the app instance when the script is executed directly
if __name__ == "__main__":
    app = create_app()  # Call the function to create the app
    print("Starting the Flask server...")
    app.run(debug=True)


