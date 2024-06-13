import pytest
import json
from app import app

def test_get_animals(client):
    response = client.get('/api/animals')
    assert response.status_code == 200
    data = json.loads(response.data.decode('utf-8'))
    assert 'name' in data
    assert 'email' in data

def test_post_animals(client):
    data = {
        'name': 'Jane Doe',
        'email': 'jane.doe@example.com'
    }
    response = client.post('/api/animals', json=data)
    assert response.status_code == 201
    assert b'success' in response.data
