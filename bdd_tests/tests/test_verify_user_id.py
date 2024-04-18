import pytest
from pytest_bdd import scenario


@scenario("../features/user_id.feature",
          "Verifying a user creation returns a non-null ID and correct timestamp")
def test_id():
    pass

@pytest.fixture()
def base_uri():
    return 'https://reqres.in/api/'
