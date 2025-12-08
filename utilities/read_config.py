import configparser
import os

config = configparser.RawConfigParser()
config_path = os.path.join(os.getcwd(), 'config.ini')
config.read(config_path)

class ReadConfig:
    @staticmethod
    def get_application_url():
        return config.get('common info', 'base_url')

    # --- NEW METHOD ---
    @staticmethod
    def get_api_url():
        try:
            return config.get('common info', 'api_url')
        except:
            return None

    @staticmethod
    def get_browser_name():
        return config.get('common info', 'browser')
        
    @staticmethod
    def get_wait_time():
        try:
            return int(config.get('common info', 'implicit_wait'))
        except:
            return 10