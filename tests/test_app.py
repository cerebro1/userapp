import pytest
from app import app
from datetime import datetime

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_homepage_loads(client):
    """Check if the homepage loads successfully"""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello" in response.data  # checks greeting is present

def test_username_display(client):
    """Check if the username is included in JSON response"""
    response = client.get('/')
    assert response.status_code == 200
    
    data = response.get_json()
    assert "message" in data
    assert "Hello Guest" in data["message"]

def test_datetime_display(client):
    """Check if current date and time appear"""
    response = client.get('/')
    now = datetime.now().strftime("%Y-%m-%d")  # just check date substring
    assert bytes(now, 'utf-8') in response.data