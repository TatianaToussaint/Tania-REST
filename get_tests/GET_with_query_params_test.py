import pytest
import requests
import json

from deepdiff import DeepDiff


@pytest.fixture
def setup():
    return {
        "base_uri": "https://jsonplaceholder.typicode.com",
        "base_path": "/comments",
        "query_params": {"postId": 6}
    }
def test_with_query_params(setup):
    response = requests.get(setup["base_uri"] + setup["base_path"], params=setup["query_params"])
    body = response.json()
    print('/', body)
    print(json.dumps(body, indent = 4))
    assert len(body) == 5

    with open("../json_expect/GET_with_query_params_test.json") as f:
        body_exp = json.load(f)
        #diff = DeepDiff(body, body_exp, exclude_paths="root[0]['postId']")
        diff = DeepDiff(body, body_exp, exclude_regex_paths="\['postId'\]")

        assert len(diff) == 0
