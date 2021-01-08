from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_get_popular_forum():
    response = client.get("/api/v1/popular-forum")
    message = response.json()
    assert response.status_code == 200
    assert len(message['message']) == 20
    for e in message['message']:
        assert 'board_name' in e
        assert 'board_nuser' in e
    