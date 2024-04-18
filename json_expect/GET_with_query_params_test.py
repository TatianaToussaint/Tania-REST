import pytest
import requests
import json


@pytest.fixture
def setup():
    return {
        "base_uri": "https://jsonplaceholder.typicode.com",
        "base_path": "/comments",
        "query_params": {"postId": 6}
    }
def test_with_query_params(setup):
    response = requests.get(setup["base_uri"] + setup["base_path"], params=setup["query_params"])
    body = response.json()
    with open("GET_with_query_params_test.json", "w") as f:
        json.dump(body, f, indent=4)