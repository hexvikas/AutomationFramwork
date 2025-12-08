import requests
from dotenv import load_dotenv
import os

load_dotenv()

class BaseAPI:
    def __init__(self):
        self.base_url = os.getenv("BASE_URL")
        self.api_key = os.getenv("OPENWEATHER_API_KEY")

    def get(self, endpoint, params=None):
        if params is None:
            params = {}

        # Auto-add API key
        params["appid"] = self.api_key
        # test api call
        response = requests.get(f"{self.base_url}{endpoint}", params=params)
        return response
