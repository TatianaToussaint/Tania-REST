import json

import pytest
import requests

from utils.file_utils import get_rows


@pytest.fixture
def base_uri():
    return "https://airportgap.com/api"


def test_osaka_airport(base_uri):
    endpoint = "/airports/KIX"
    response = requests.get(base_uri + endpoint)

    body = response.json()
    print("\n", json.dumps(body, indent= 4))


@pytest.mark.parametrize("airport, country", get_rows("airports.csv"))
def test_airports(base_uri, airport, country):
    endpoint = "/airports/" + airport
    response = requests.get(base_uri + endpoint)

    body = response.json()
    assert body["data"]["attributes"]["country"] == country.strip()