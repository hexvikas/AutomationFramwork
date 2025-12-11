import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class DriverFactory:

    @staticmethod
    def create_driver():
        options = Options()

        # If running inside Jenkins → Enable headless mode
        if os.environ.get("JENKINS_HOME"):
            print("Running inside Jenkins → Headless mode ON")
            options.add_argument("--headless=new")
            options.add_argument("--disable-gpu")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--window-size=1920,1080")
        else:
            print("Running locally → Browser will open normally")

        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        driver.maximize_window()
        return driver
