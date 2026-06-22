import pytest
from flask import Flask

import views
from models import Client, Itinerary

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

@pytest.fixture
def test_itineraries():
    return [
        Itinerary(id=101, client_id=1, destination="test destination", start_date="2026-02-12", end_date="2026-02-28"),
        Itinerary(id=101, client_id=1, destination="test destination", start_date="2026-02-12", end_date="2026-02-28", activities="kayaking, sightseeing"),
        Itinerary(id=101, client_id=11, destination="test destination", start_date="2026-02-12", end_date="2026-02-28")
    ]

@pytest.fixture
def test_itineraries_json():
    return [
        {"id": 101, "client_id": 1, "destination": "test destination", "start_date": "2026-02-12", "end_date": "2026-02-28"},
        {"id": 101, "client_id": 1, "destination": "test destination", "start_date": "2026-02-12", "end_date": "2026-02-28", "activities": "kayaking, sightseeing"},
        {"id": 101, "client_id": 11, "destination": "test destination", "start_date": "2026-02-12", "end_date": "2026-02-28"},
    ]

@pytest.fixture()
def test_app_client():
    app = Flask(__name__)
    app.register_blueprint(views.bp)
    with app.test_client() as client:
        yield client
