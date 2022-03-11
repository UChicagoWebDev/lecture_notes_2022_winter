import pytest
import passwords

@pytest.fixture
def client():
    server = passwords.create_app()
    with server.test_client() as client:
        yield client


def test_admin_forbidden(client):
    """Returns a 403 to calls without the correct secret password"""
    response = client.post('/api/admin', json={})
    assert response.status == "403 FORBIDDEN"

    response = client.post('/api/admin', json={'secret_code': 'konami'})
    assert response.status == "403 FORBIDDEN"

def test_admin_with_code(client):
    """Returns a 200 to calls with the correct secret password"""
    response = client.post('/api/admin', json={'secret_code': 'open sesame'})
    assert response.status == "200 OK"
