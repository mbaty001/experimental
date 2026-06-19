import pytest
from flask import Flask

import views
from models import Client

@pytest.fixture
def test_clients():
    return (
        Client(id=1, name="Alice", email="alice@example.com", phone="123", address="Addr1"),
        Client(id=2, name="Bob", email="bob@example.com", phone=None, address="Addr2"),
    )

@pytest.fixture()
def test_clients_json():
    return [
        {"id": 1, "name": "Alice", "email": "alice@example.com", "phone": "123", "address": "Addr1"},
        {"id": 2, "name": "Bob", "email": "bob@example.com", "phone": None, "address": "Addr2"},
    ]

@pytest.fixture()
def test_app_client():
    app = Flask(__name__)
    app.register_blueprint(views.bp)
    with app.test_client() as client:
        yield client
