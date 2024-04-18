import pytest
import requests


@pytest.fixture
def base_uri():
    return "http://jsonplaceholder.typicode.com"

def test_put(base_uri):
    endpoint = "/posts/1"
    headers = {"Content-Type": "application/json"}
    payload = {
        "id": 1,
        "title": "Real SQA",
        "body": "Python",
        "userId": 1
    }

    response = requests.put(base_uri + endpoint, json= payload, headers= headers)
    print("\nResponse content:", response.text)
    body = response.json()
    assert body["title"] == "Real SQA"