from utils.request_helper import RequestHelper
from utils.assertions import assert_status_code, assert_response_contains
from data.test_data import update_payload

request = RequestHelper()

def test_update_user():
    user_id = 2  
    response = request.put(f"/api/users/{user_id}", data=update_payload)

    assert_status_code(response, 200)
    assert_response_contains(response, ["name", "job", "updatedAt"])
