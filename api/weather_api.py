from api.base_api import BaseAPI

class WeatherAPI(BaseAPI):

    def get_current_weather(self, city):
        return self.get("/weather", {"q": city})

    def get_forecast(self, city):
        return self.get("/forecast", {"q": city})

    def get_invalid_key(self, city):
        return self.get("/weather", {"q": city, "appid": "invalid_key_123"})
