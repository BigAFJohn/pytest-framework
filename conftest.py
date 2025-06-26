import pytest
from utils.request_helper import RequestHelper

@pytest.fixture(scope="session")
def http_request():
    return RequestHelper()
