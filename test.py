from app import app


def testApp():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert response.data == b'Example app'