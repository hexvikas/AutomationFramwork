import configparser
import os

class ReadConfig:

    config = configparser.RawConfigParser()

    # Always read config relative to project root
    config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config", "config.ini")
    config.read(config_path)

    @staticmethod
    def get_application_url():
        return ReadConfig.config.get("common", "baseURL")

    @staticmethod
    def get_browser():
        return ReadConfig.config.get("common", "browser")

    # ---------------- API READERS ----------------
    @staticmethod
    def get_weather_api_url():
        return ReadConfig.config.get("api", "weather_api_url")

    @staticmethod
    def get_weather_api_key():
        return ReadConfig.config.get("api", "api_key")
