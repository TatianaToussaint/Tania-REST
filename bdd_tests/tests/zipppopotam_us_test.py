import pytest
import requests
from pytest_bdd import scenario, given, when, then


@pytest.fixture
def base_uri():
    return {"uri": ""}

@pytest.fixture()
def response():
    return {"get": ""}

@scenario("../features/zippopotam_us.feature",
          "Submit a GET request with a country zip code")

def test_with_zipcode():
    pass

@given("base uri is 'http://api.zippopotam.us'")
def get_base_uri(base_uri):
    base_uri["uri"] = 'http://api.zippopotam.us'

@given ("zip code is 94404")
@when("GET request is submitted to the endpoint '/us/94404'")
def submit_GET(base_uri, response):
    endpoint = '/us/94404'
    get_response = requests.get(base_uri["uri"] + endpoint)
    response["get"] = get_response

@then("response status code is 200")
def verify_status_code(response):
    assert response["get"].status_code == 200

@then("response 'Content_type' header is 'application/json'")
def verify_content_type_header(response):
    content_type = response["get"].headers.get("Content-Type")
    assert content_type == "application/json"

@then("'place name' is 'San Moteo'")
def verify_place_name(response):
    body = response["get"].json()
    assert body["places"][0]['place name'] == "San Mateo"

@then("'state' is 'California'")
def verify_state(response):
    body = response["get"].json()
    assert body["places"][0]['state'] == "California"

@scenario("../features/zippopotam_us.feature",
          "Submit a GET request with a city name")

def test_with_city():
    pass

@given("city is 'San Mateo'")
@when("GET request is submitted to the endpoint '/us/ca/San Mateo'")
def send_GET(base_uri, response):
    endpoint = '/us/ca/San Mateo'
    get_response = requests.get(base_uri["uri"] + endpoint)
    response["get"] = get_response

@then("'places' list has 9 objects")
def verify_number_of_places_objects(response):
    body = response["get"].json()
    assert len(body["places"]) == 9