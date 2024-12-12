import os
import pytest
from backend import create_app, db

os.environ['FLASK_ENV'] = 'testing'
os.environ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_water_monitoring.db'

app = create_app()

@pytest.fixture(scope='module')
def setup_db():
    db.init_app(app)
    app.app_context().push()
    db.create_all()
    yield db
    db.session.remove()
    db.drop_all()

@pytest.fixture(scope='module')
def client():
    with app.test_client() as client:
        yield client
