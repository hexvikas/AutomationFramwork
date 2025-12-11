import json
import os
from appium import webdriver

class AndroidDriver:

    def __init__(self, caps_path: str | None = None):
        if caps_path is None:
            caps_path = os.path.join(os.getcwd(), "android_caps.json")
        with open(caps_path, "r") as f:
            cfg = json.load(f)

        self.server_url = cfg["server_url"]
        self.caps = cfg["capabilities"]

    def get_driver(self):
        driver = webdriver.Remote(
            command_executor=self.server_url,
            desired_capabilities=self.caps
        )
        return driver
