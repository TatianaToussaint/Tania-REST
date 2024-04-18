import pytest
import requests
from pytest_bdd import scenario, given, when, then


@pytest.fixture
def base_uri():
    return {"uri": ""}


@pytest.fixture()
def response():
    return {"get": ""}


@scenario("../features/user_information.feature",
          "Retrieve user with ID 8 and verify last name and URL in the response")


def test_last_name_user_id8():
    pass


@given("base uri is 'https://reqres.in/api'")
def get_base_uri(base_uri):

    base_uri["uri"] = 'https://reqres.in/api'

@given("endpoint '/users/8'")
@when("send a GET request to the endpoint")
def submit_get(base_uri, response):
    endpoint = '/users/8'
    get_response = requests.get(base_uri["uri"] + endpoint)
    response["get"] = get_response


@then("response status code is 200")
def verify_status_code(response):
    assert response["get"].status_code == 200


@then("The response to contain JSON")
def verify_content_type_header(response):
    content_type = response["get"].headers.get("Content-Type")
    assert "application/json" in content_type


@then("The JSON response should have 'last_name' with value 'Ferguson'")
def verify_last_name(response):
    json_response = response["get"].json()
    assert json_response['data']['last_name'] == "Ferguson"


@then("The JSON response should have 'url' with value 'https://reqres.in/#support-heading'")
def verify_url(response):
    json_response = response["get"].json()
    assert json_response['support']['url'] == "https://reqres.in/#support-heading"
