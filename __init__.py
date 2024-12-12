from flask import Flask
from .factory import create_app

def init_app():
    app = create_app()
    return app
