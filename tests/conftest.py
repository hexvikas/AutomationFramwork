import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from api.base_api import APIClient
from utilities.read_config import ReadConfig
from utilities.custom_logger import LogGen

# Appium drivers
from mobile.drivers.android_driver import AndroidDriver   # <-- make sure file name is android_driver.py

logger = LogGen.loggen()


def pytest_addoption(parser):
    parser.addoption(
        "--platform",
        action="store",
        default="web",
        help="Choose platform: web or android"
    )


@pytest.fixture(scope="class")
def setup(request):
    """
    UNIVERSAL DRIVER FIXTURE:
    - Selenium for Web UI
    - Appium for Mobile Web / Mobile App
    """
    platform = request.config.getoption("--platform")
    logger.info(f"=== Starting test on platform: {platform} ===")

    driver = None

    # ------------------------------------
    # WEB PLATFORM (Selenium)
    # ------------------------------------
    if platform == "web":
        browser = ReadConfig.getBrowser()

        if browser.lower() == "chrome":
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        else:
            raise Exception("Only Chrome browser supported currently")

        driver.maximize_window()
        driver.implicitly_wait(10)

        base_url = ReadConfig.getApplicationURL()
        logger.info(f"Navigating to Web URL: {base_url}")
        driver.get(base_url)

    # ------------------------------------
    # ANDROID PLATFORM (Appium)
    # ------------------------------------
    elif platform == "android":
        logger.info("Initializing Android Appium driver...")
        driver = AndroidDriver().get_driver()

        base_url = ReadConfig.getApplicationURL()
        logger.info(f"Navigating to Mobile URL: {base_url}")
        driver.get(base_url)

    else:
        raise Exception(f"Invalid platform: {platform}")

    # Attach driver to class
    request.cls.driver = driver

    yield

    logger.info("Closing driver session...")
    driver.quit()
    logger.info("=== Test session ended ===")


@pytest.fixture(scope="session")
def api_client():
    """Shared API client for API test cases."""
    return APIClient()
