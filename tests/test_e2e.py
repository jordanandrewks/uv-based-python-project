from fastapi.testclient import TestClient

import pytest

from new_service.views import app

@pytest.fixture(name="client")
def _client():
    return TestClient(app)

def test_hello(client):
    """
    Root URL greets the world.
    """
    response = client.get("/")

    assert 200 == response.status_code
    assert {
        'message': 'Hello World'
    } == response.json()


    # send response to webview and get a response.

    