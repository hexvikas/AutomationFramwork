from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os


class DriverFactory:

    @staticmethod
    def create_driver():
        """Creates and returns a configured Chrome WebDriver instance."""

        options = Options()
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-notifications")
        options.add_argument("--start-maximized")

        # Jenkins CI mode
        if os.getenv("JENKINS_HOME"):
            options.add_argument("--headless=new")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-gpu")
            options.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Chrome(
            service=webdriver.ChromeService(ChromeDriverManager().install()),
            options=options
        )

        return driver
