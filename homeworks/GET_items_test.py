import json
import pytest
import requests


@pytest.fixture
def setup():
    return {
        "base_uri": "https://reqres.in",
        "endpoint": "/api/unknown"
    }

def test_items_count(setup):
    response = requests.get(setup["base_uri"] + setup["endpoint"])
    body = response.json()
    print('/n',json.dumps(body, indent =4))

    assert response.status_code == 200
    assert response.ok

    assert len(body["data"]) == 6
