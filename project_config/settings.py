import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    @staticmethod
    def get_base_url():
        return os.getenv("BASE_URL", "https://reqres.in")

    @staticmethod
    def get_api_key():
        return os.getenv("REQRES_API_KEY")
