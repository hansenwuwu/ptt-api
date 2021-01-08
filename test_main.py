from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_get_popular_forum():
    response = client.get("/api/v1/forum/popular")
    message = response.json()
    assert response.status_code == 200
    assert len(message['message']) == 20
    for e in message['message']:
        assert 'board_name' in e
        assert 'board_nuser' in e
    return message['message']

def test_get_forum_page():
    popular_forum_list = test_get_popular_forum()
    
    for e in popular_forum_list:
        board_name = e['board_name']
        page = 5
        response = client.get("/api/v1/forum/" + board_name + '?page=' + str(page))
        message = response.json()
        assert response.status_code == 200
        # assert message == {"message": board_name, "page": page}
        break
    

