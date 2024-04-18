import pytest
import requests
import json

@pytest.fixture
def base_uri():
    return "https://reqres.in/api"

def test_last_name(base_uri):
    endpoint = "/users/8"
    response = requests.get(base_uri + endpoint)

    body = response.json()

    print(json.dumps(body, indent=4))

    assert body["data"]["last_name"] == "Ferguson"
    assert body["support"]["url"] == "https://reqres.in/#support-heading"