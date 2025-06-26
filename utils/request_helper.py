import requests
from project_config.settings import Config

class RequestHelper:
    def __init__(self, base_url=None):
        self.base_url = base_url or Config.get_base_url()
        api_key = Config.get_api_key()
        self.headers = {"x-api-key": api_key} if api_key else {}

    def get(self, endpoint, params=None):
        return requests.get(f"{self.base_url}{endpoint}", params=params, headers=self.headers)

    def post(self, endpoint, data=None):
        return requests.post(f"{self.base_url}{endpoint}", json=data, headers=self.headers)

    def put(self, endpoint, data=None):
        return requests.put(f"{self.base_url}{endpoint}", json=data, headers=self.headers)

    def patch(self, endpoint, data=None):
        return requests.patch(f"{self.base_url}{endpoint}", json=data, headers=self.headers)

    def delete(self, endpoint):
        return requests.delete(f"{self.base_url}{endpoint}", headers=self.headers)
