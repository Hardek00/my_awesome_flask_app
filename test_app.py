import pytest
from app import app


@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_hello_endpoint(client):
    """Test the hello endpoint."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello, welcome to my flask_app" in response.data


def test_bye_endpoint(client):
    """Test the bye endpoint."""
    response = client.get('/bye')
    assert response.status_code == 200
    assert b"Goodbye my friend" in response.data


def test_hau_endpoint(client):
    """Test the hau endpoint."""
    response = client.get('/hau')
    assert response.status_code == 200
    assert b"How are you" in response.data


def test_nonexistent_endpoint(client):
    """Test that nonexistent endpoints return 404."""
    response = client.get('/nonexistent')
    assert response.status_code == 404
