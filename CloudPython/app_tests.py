from app import app
import pytest

@pytest.fixture(scope='function', name="appl")
def setup():
    appl = app.test_client() 
    appl.testing = True
    return appl
    
@pytest.mark.parametrize("uri, expected_status_code",
                        [('/api/v1/users', 200),
                         ('/api/v2/tweets', 200),
                         ('/api/v3/fail', 404)])
def test_status_code(appl, uri, expected_status_code): 
    result = appl.get(uri)
    assert result.status_code == expected_status_code

def test_addusers_status_code(appl):
    result = appl.post('/api/v1/users', data='{"username":"test_user",\
                                               "name":"Jon Bon Jovi",\
                                               "email":"jon.bonjovi@gmail.com",\
                                               "password":"passwd"}',
                                        content_type = 'application/json')
    print (result)
    assert result.status_code == 201 or result.status_code == 409

def test_updusers_status_code(appl):
    result = appl.put('/api/v1/users/2', data='{"password":"testing123"}',
                                         content_type = 'application/json')
    print (result)
    assert result.status_code == 200
