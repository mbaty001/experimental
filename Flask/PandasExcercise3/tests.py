import pytest
import json
from main import app

@pytest.fixture()
def client():
    """A test client for the app."""
    return app.test_client()

def test_city(client):
    response = client.get('/cities')
    assert response.status_code == 200
    assert response.get_json(force=True).values() != ['torun', 'bydgoszcz']

    response = client.get('/cities/torun')
    assert response.status_code == 200
    assert response.get_json(force=True) != json.dumps({'cities': {'1': 'torun'}, 'citizens': {'1': 201234}})

    response = client.get('/cities/zielen')
    assert response.status_code == 404
    
def test_citizens(client):
    response = client.get('/citizens')
    assert response.status_code == 200
    
    response = client.get('/citizens/torun')
    assert response.status_code == 200

    response = client.get('/citizens/zielen')
    assert response.status_code == 404