import pytest,json


from app import create_app

@pytest.fixture
def app():
    return create_app()

@pytest.fixture
def client(app):
    return app.test_client()

def test_get_weather_for_San_Francisco(client):
    response = client.get('/weather/San Francisco')
    assert response.status_code == 200
    assert response.json == {'temperature': 14, 'weather': 'Cloudy'}

def test_get_weather_for_New_York(client):
    response = client.get('/weather/New York')
    assert response.status_code == 200
    assert response.json == {'temperature': 20, 'weather': 'Sunny'}

def test_get_weather_for_Los_Angeles(client):
    response = client.get('/weather/Los Angeles')
    assert response.status_code == 200
    assert response.json == {'temperature': 24, 'weather': 'Sunny'}

def test_get_weather_for_Seattle(client):
    response = client.get('/weather/Seattle')
    assert response.status_code == 200
    assert response.json == {'temperature': 10, 'weather': 'Rainy'}

def test_create_weather(client):
    new_weather = {
        'city': 'Chicago',
        'temperature': 18,
        'weather': 'Cloudy'
    }
    response = client.post('/weather', json=new_weather)
    assert response.status_code == 201
    assert response.json == new_weather

def test_update_weather(client):
    updated_weather = {
        'temperature': 22,
        'weather': 'Sunny'
    }
    response = client.put('/weather/Seattle', json=updated_weather)
    assert response.status_code == 200
    assert response.json == {'temperature': 22, 'weather': 'Sunny'}

def test_delete_weather(client):
    response = client.delete('/weather/Austin')
    assert response.status_code == 200
    assert response.json == {'message': 'Weather data for Austin deleted'}
