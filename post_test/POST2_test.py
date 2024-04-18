import json

import pytest
import requests


@pytest.fixture
def base_uri():
    return "https://petstore.swagger.io/v2"

def test_post(base_uri):
    endpoint = "/pet"
    headers = {"Content-Type": "application/json"}
    payload = {
      "id": 0,
      "category": {
        "id": 0,
        "name": "string"
      },
      "name": "cat",
      "photoUrls": [
        "string"
      ],
      "tags": [
        {
          "id": 0,
          "name": "string"
        }
      ],
      "status": "available"
    }

    response = requests.post(base_uri + endpoint, json= payload, headers = headers)
    print(response.text)
    body= response.json()
    # assert body ["id"] != "9223372036854605991"
    assert body["id"] != "0"
    assert body["id"] is not None

    assert "922337203685460" in str(body["id"])
    assert body["name"] == "cat"