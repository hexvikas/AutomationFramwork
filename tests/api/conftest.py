import pytest
from utilities.custom_logger import LogGen
from api.base_api import BaseAPI

logger = LogGen.loggen()


@pytest.fixture(scope="session")
def api_client():
    """API client fixture for API tests"""
    client = BaseAPI()
    logger.info("✅ API client initialized")
    return client


@pytest.fixture(scope="function")
def api_response(api_client):
    """API response handler fixture"""
    class APIResponseHandler:
        def __init__(self, client):
            self.client = client
            self.last_response = None

        def assert_status_code(self, response, expected_code):
            """Assert response status code"""
            assert response.status_code == expected_code, \
                f"Expected {expected_code}, got {response.status_code}"
            self.last_response = response
            return response

        def assert_json_contains(self, response, key):
            """Assert response JSON contains key"""
            data = response.json()
            assert key in data, f"Key '{key}' not found in response"
            return data

    return APIResponseHandler(api_client)
