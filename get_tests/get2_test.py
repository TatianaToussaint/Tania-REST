import pytest
import requests


@pytest.fixture
def base_uri():
    return "https://jsonplaceholder.typicode.com"


def test_users(base_uri):
    endpoint = "/users"
    response = requests.get(base_uri + endpoint)

    body = response.json()
    assert body[0]["username"] == "Bret"

    usernames = []
    for user in body:
        usernames.append(user["username"])
    print("\n" + str(usernames))

    assert "Bret" and "Samantha" in usernames

    assert len(body) == 10