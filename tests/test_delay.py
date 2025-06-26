import time
from utils.request_helper import RequestHelper
from utils.assertions import assert_status_code, assert_response_contains
from data.test_data import delayed_request_params

request = RequestHelper()

def test_delayed_response():
    start_time = time.time()

    response = request.get("/api/users", params=delayed_request_params)

    end_time = time.time()
    elapsed = end_time - start_time

    assert_status_code(response, 200)
    assert_response_contains(response, ["data"])
    assert elapsed <= 3.5, f"Response took too long: {elapsed:.2f} seconds"
