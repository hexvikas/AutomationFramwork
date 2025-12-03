import configparser
import os

config = configparser.RawConfigParser()
config_path = os.path.join(os.getcwd(), 'config.ini')
config.read(config_path)

class ReadConfig:
    @staticmethod
    def get_application_url():
        url = config.get('common info', 'base_url')
        return url

    @staticmethod
    def get_browser_name():
        browser = config.get('common info', 'browser')
        return browser

    @staticmethod
    def get_wait_time():
        try:
            return int(config.get('common info', 'implicit_wait'))
        except:
            return 10