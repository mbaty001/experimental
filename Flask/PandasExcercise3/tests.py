import pytest
from main import app

@pytest.fixture()
def client():
    """A test client for the app."""
    return app.test_client()

def test_hello(client):
    response = client.get('/hello')
    assert response.status_code == 200