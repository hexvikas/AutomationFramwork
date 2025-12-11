from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
import os
import json
from utilities.read_config import ReadConfig


class AppiumDriver:
    """Manages Appium driver initialization for mobile testing"""

    def __init__(self, platform="android"):
        self.platform = platform.lower()
        self.driver = None

    def get_driver(self):
        """Get Appium driver instance"""
        if self.platform == "android":
            return self._create_android_driver()
        elif self.platform == "ios":
            return self._create_ios_driver()
        else:
            raise ValueError(f"Unsupported platform: {self.platform}")

    def _create_android_driver(self):
        """Create Android driver"""
        caps_file = os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
            "config", "capabilities", "android_caps.json"
        )

        with open(caps_file, 'r') as f:
            caps = json.load(f)

        options = UiAutomator2Options()
        for key, value in caps.items():
            options.set_capability(key, value)

        appium_server_url = "http://localhost:4723"
        self.driver = webdriver.Remote(appium_server_url, options=options)
        return self.driver

    def _create_ios_driver(self):
        """Create iOS driver"""
        caps_file = os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
            "config", "capabilities", "ios_caps.json"
        )

        with open(caps_file, 'r') as f:
            caps = json.load(f)

        options = XCUITestOptions()
        for key, value in caps.items():
            options.set_capability(key, value)

        appium_server_url = "http://localhost:4723"
        self.driver = webdriver.Remote(appium_server_url, options=options)
        return self.driver

    def quit_driver(self):
        """Quit driver session"""
        if self.driver:
            self.driver.quit()
