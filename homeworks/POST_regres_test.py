import json
import pytest
import requests


@pytest.fixture
def base_uri():
    return "https://reqres.in/api"

def test_post(base_uri):
    endpoint = "/users"
    headers = {"Content-Type": "application/json"}
    payload = {
        "name": "Tania",
        "job": "Student"
}
    response = requests.post(base_uri + endpoint, json=payload, headers=headers)
    print(response.text)
    body = response.json()

    assert response.status_code == 201
    assert body["id"] is not None
    assert "2024-03-" in str(body["createdAt"])