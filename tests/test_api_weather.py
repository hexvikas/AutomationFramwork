import pytest
from api.weather_api import WeatherAPI

class TestWeatherAPI:

    @pytest.fixture()
    def weather(self):
        return WeatherAPI()   # Create instance before each test

    def test_get_weather_valid_city(self, weather):
        response = weather.get_current_weather("London")
        data = response.json()

        print("\nResponse:", data)

        assert response.status_code == 200
        assert data["name"] == "London"
        assert "main" in data

    def test_get_weather_invalid_city(self, weather):
        response = weather.get_current_weather("ThisCityDoesNotExist123")
        data = response.json()

        assert response.status_code == 404
        assert data["message"] == "city not found"

    def test_invalid_api_key(self, weather):
        response = weather.get_invalid_key("Goa")
        data = response.json()

        assert response.status_code == 401
        assert "Invalid API key" in data["message"]

    def test_weather_in_metric_units(self, weather):
        response = weather.get_current_weather("Delhi")
        data = response.json()

        assert response.status_code == 200
        temp = data["main"]["temp"]

        assert -50 < temp < 60

    def test_forecast_schema_structure(self, weather):
        response = weather.get_forecast("Mumbai")
        data = response.json()

        assert response.status_code == 200
        assert "cnt" in data
        assert "list" in data
        assert isinstance(data["list"], list)
        assert len(data["list"]) > 0
