
def assert_status_code(response, expected_code):
    assert response.status_code == expected_code, \
        f"Expected status code {expected_code}, got {response.status_code}"

def assert_response_contains(response, expected_keys):
    json_data = response.json()
    missing_keys = [key for key in expected_keys if key not in json_data]
    assert not missing_keys, \
        f"Missing keys in response: {missing_keys}"

def assert_response_equals(response, expected_data):
    json_data = response.json()
    assert json_data == expected_data, \
        f"Expected response {expected_data}, got {json_data}"

def assert_key_value(response, key, expected_value):
    json_data = response.json()
    assert json_data.get(key) == expected_value, \
        f"Expected {key} to be {expected_value}, got {json_data.get(key)}"
