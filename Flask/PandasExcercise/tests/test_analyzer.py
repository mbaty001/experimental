from analyzer import create_app

def test_hello(client):
    response = client.get('/hello')
    assert response.status_code == 200