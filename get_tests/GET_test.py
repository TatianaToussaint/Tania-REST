import json
from http import HTTPStatus

import pytest
import requests
from deepdiff import DeepDiff


@pytest.fixture
def setup():
    return {
        "base_uri": "http://api.zippopotam.us",
        "zip": 94404,
        "city": "San Mateo"
    }


def test_zipcode(setup):
    endpoint = "/us/" + str(setup["zip"])
    response = requests.get(setup["base_uri"] + endpoint)

    assert response.status_code == 200
    assert response.ok

    content_type = response.headers.get("Content-Type")
    print(content_type)
    assert content_type =="application/json"

    body = response.json()
    assert int(body["post code"]) == setup["zip"]
    # print("\n", json.dumps(body, indent=4))

    assert body["places"][0]['place name'] == "San Mateo"
    assert body["places"][0]['state'] == "California"
    for key in body:
        print(key, ":", body[key])

    #_________________________________________________
    #diff json object

    with open("../json_expect/GET_test.json") as f:
        body_exp = json.load(f)

        diff = DeepDiff(body,body_exp, exclude_paths=[
            "root['places'][0]['state']",
            "root['places'][0]['place name']"])
        print(diff)
        assert len(diff) == 0


def test_city(setup):
    endpoint = "/us/ca/" + setup["city"]
    response = requests.get(setup["base_uri"] + endpoint)

    assert response.status_code == HTTPStatus.OK
    body = response.json()
    print('/n',json.dumps(body, indent =4))



    