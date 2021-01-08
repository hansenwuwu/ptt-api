from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/api/v1/popular-forum")
    assert response.status_code == 200
    message = response.json()
    assert len(message['message']) == 20