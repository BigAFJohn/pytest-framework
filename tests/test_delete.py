# tests/test_delete.py

from utils.request_helper import RequestHelper
from utils.assertions import assert_status_code

request = RequestHelper()

def test_delete_user():
    response = request.delete("/api/users/2")

    assert_status_code(response, 204)
