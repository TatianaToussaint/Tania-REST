import json

import pytest
import requests


@pytest.fixture
def setup():
    return {
        "base_uri": "http://api.zippopotam.us",
        "zip": 94404
    }


def test_zipcode(setup):
    endpoint = "/us/" + str(setup["zip"])
    response = requests.get(setup["base_uri"] + endpoint)
    body = response.json()

    with open("GET_test.json", "w") as f:
        json.dump(body, f, indent= 4)