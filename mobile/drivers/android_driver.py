from appium.webdriver import Remote
import json
import os


class AndroidDriver:

    def __init__(self, caps_path: str | None = None):
        # Load capabilities JSON file
        if caps_path is None:
            caps_path = os.path.join(os.getcwd(), "android_caps.json")

        with open(caps_path, "r") as f:
            cfg = json.load(f)

        self.server_url = cfg["server_url"]
        self.caps = cfg["capabilities"]

    def get_driver(self):
        """Create and return Appium Android driver instance"""
        driver = Remote(
            command_executor=self.server_url,
            desired_capabilities=self.caps
        )
        return driver
