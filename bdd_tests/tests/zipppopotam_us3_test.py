import pytest
import requests
from pytest_bdd import scenario, given, when, then


@scenario("../features/zippopotam_us.feature",
          "Submit a GET request with a country zip code")
def test_with_zipcode():
    pass


@pytest.fixture()
@given("base uri is 'http://api.zippopotam.us'")
def base_uri():
    return 'http://api.zippopotam.us'


@given("zip code is 94404")
@when("GET request is submitted to the endpoint '/us/94404'")
def GET_response(base_uri):
    endpoint = '/us/94404'
    pytest.response = requests.get(base_uri + endpoint)


@then("response status code is 200")
def verify_status_code():
    assert pytest.response.status_code == 200


@then("response 'Content_type' header is 'application/json'")
def verify_content_type_header():
    content_type = pytest.response.headers.get("Content-Type")
    assert content_type == "application/json"


@then("'place name' is 'San Moteo'")
def verify_place_name():
    body = pytest.response.json()
    assert body["places"][0]['place name'] == "San Mateo"


@then("'state' is 'California'")
def verify_state():
    body = pytest.response.json()
    assert body["places"][0]['state'] == "California"


@scenario("../features/zippopotam_us.feature",
          "Submit a GET request with a city name")
def test_with_city():
    pass


@given("city is 'San Mateo'")
@when("GET request is submitted to the endpoint '/us/ca/San Mateo'")
def response_GET(base_uri):
    endpoint = '/us/ca/San Mateo'
    pytest.response = requests.get(base_uri + endpoint)


@then("'places' list has 9 objects")
def verify_number_of_places_objects():
    body = pytest.response.json()
    assert len(body["places"]) == 9
