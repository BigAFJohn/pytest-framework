from utils.request_helper import RequestHelper
from utils.assertions import assert_status_code, assert_response_contains
from data.test_data import valid_login_payload

request = RequestHelper()

def test_successful_login():
    response = request.post("/api/login", data=valid_login_payload)

    assert_status_code(response, 200)
    assert_response_contains(response, ["token"])
