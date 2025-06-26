
# ✅ Login
valid_login_payload = {
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
}

invalid_login_payload = {
    "email": "peter@klaven"
}

# ✅ Update
update_payload = {
    "name": "morpheus",
    "job": "zion resident"
}

# ✅ Create (optional, but used to support DELETE/PUT)
create_user_payload = {
    "name": "John",
    "job": "Engineer"
}

# ✅ Negative test cases
nonexistent_user_id = 9999
missing_fields_login = {
    "email": ""
}

# ✅ Delayed request
delayed_request_params = {
    "delay": 3  # Max 3 seconds
}
