import json

import pytest
import requests


@pytest.fixture
def base_uri():
    return "https://postman-echo.com"

def test_post(base_uri):
    endpoint = "/post"
    headers = {"Content-Type": "application/json"}
    payload = {
                "name": "Tania",
                "relation": "student"
}

    response = requests.post(base_uri + endpoint, json=payload, headers=headers)

    body = response.json()
    print("\n", json.dumps(body, indent=4))

    assert response.status_code == 200
    assert body["json"]["name"] == "Tania"
