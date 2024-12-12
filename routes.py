# backend/routes.py
from flask import Blueprint

bp = Blueprint('main', __name__)

@bp.route('/status', methods=['GET'])
def status():
    return {"status": "Water Monitoring API is running!"}

@bp.route('/', methods=['GET'])
def index():
    return "Welcome to the Water Monitoring API"

