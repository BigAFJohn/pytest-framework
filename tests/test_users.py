import pytest
from utils.request_helper import RequestHelper
from utils.assertions import assert_status_code, assert_response_contains

request = RequestHelper()

def test_get_users_list():
    response = request.get("/api/users", params={"page": 2})

    assert_status_code(response, 200)
    data = response.json()

    assert "data" in data, "'data' key not found in response"
    assert isinstance(data["data"], list), "'data' is not a list"

    # Check each user has required keys
    for user in data["data"]:
        assert_response_contains(MockResponse(user), ["id", "email", "first_name", "last_name", "avatar"])

class MockResponse:
    def __init__(self, json_data):
        self._json_data = json_data

    def json(self):
        return self._json_data

