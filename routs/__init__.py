# backend/routes/__init__.py
from flask import Blueprint

bp = Blueprint('routes', __name__)

# Example route
@bp.route('/')
def index():
    return "Welcome to the Water Monitoring API"
