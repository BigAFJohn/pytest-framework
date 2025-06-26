from utils.request_helper import RequestHelper
from utils.assertions import assert_status_code, assert_key_value
from data.test_data import invalid_login_payload, nonexistent_user_id

request = RequestHelper()

def test_login_missing_password():
    response = request.post("/api/login", data=invalid_login_payload)

    assert_status_code(response, 400)
    assert_key_value(response, "error", "Missing password")

def test_user_not_found():
    response = request.get(f"/api/users/{nonexistent_user_id}")

    assert_status_code(response, 404)
