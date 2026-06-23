import pytest
from flask import Flask

import views
from models import Client, Itinerary


@pytest.fixture
def test_clients():
    return [
        Client(
            id=1, name="Alice", email="alice@example.com", phone="123", address="Addr1"
        ),
        Client(id=2, name="Bob", email="bob@example.com", phone=None, address="Addr2"),
    ]


@pytest.fixture
def test_clients_json(test_clients):
    return [
        {
            "id": c.id,
            "name": c.name,
            "email": c.email,
            "phone": c.phone,
            "address": c.address,
        }
        for c in test_clients
    ]


@pytest.fixture
def test_itineraries():
    return [
        Itinerary(
            id=101,
            client_id=1,
            destination="test destination",
            start_date="2026-02-12",
            end_date="2026-02-28",
        ),
        Itinerary(
            id=102,
            client_id=1,
            destination="test destination",
            start_date="2026-02-12",
            end_date="2026-02-28",
            activities="kayaking, sightseeing",
        ),  # Fixed duplicate ID
        Itinerary(
            id=103,
            client_id=11,
            destination="test destination",
            start_date="2026-02-12",
            end_date="2026-02-28",
        ),  # Fixed duplicate ID
    ]


@pytest.fixture
def test_itineraries_json(test_itineraries):
    result = []
    for iti in test_itineraries:
        d = {
            "id": iti.id,
            "client_id": iti.client_id,
            "destination": iti.destination,
            "start_date": iti.start_date,
            "end_date": iti.end_date,
        }
        # Handle optional attribute cleanly
        if hasattr(iti, "activities") and iti.activities is not None:
            d["activities"] = iti.activities
        result.append(d)
    return result


@pytest.fixture()
def test_app_client():
    app = Flask(__name__)
    app.register_blueprint(views.bp)
    with app.test_client() as client:
        yield client
