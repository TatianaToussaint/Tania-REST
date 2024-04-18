import pytest
import requests
from pytest_bdd import scenario, given, parsers, when, then


@scenario("../features/airportgap.feature",
          "Submit GET request with an airport ticker")
def test_airports():
    pass

@pytest.fixture()
def base_uri():
    return 'https://airportgap.com/api'

@given(parsers.cfparse("Airport ticker is {ticker: w}"))
@when(parsers.cfparse("GET request is submitted to the end point  /airports/{ticker}"))
def submit_GET(base_uri, ticker):
    endpoint = "/airports/" + ticker
    pytest.response = requests.get(base_uri + endpoint)

@then(parsers.cfparse("country is {country}"))
def verify_country(country):
    body = pytest.response.json()
    assert body["data"]["attributes"]["country"] == country
