import pytest
import os
from datetime import datetime
from pathlib import Path

from utilities.read_config import ReadConfig
from utilities.custom_logger import LogGen
from core.driver_factory import DriverFactory

logger = LogGen.loggen()


@pytest.fixture(scope="function")
def web_driver(request):
    """Web driver fixture for Selenium tests"""
    drv = None
    try:
        drv = DriverFactory.create_driver()
        base_url = ReadConfig.get_application_url()
        drv.get(base_url)
        logger.info(f"✅ Web driver initialized: {base_url}")
        
        yield drv

    finally:
        if drv:
            drv.quit()
            logger.info("✅ Web driver closed")


@pytest.fixture(scope="function")
def driver(request):
    """Alias fixture for backward compatibility - tests expect 'driver'"""
    drv = None
    try:
        drv = DriverFactory.create_driver()
        base_url = ReadConfig.get_application_url()
        drv.get(base_url)
        logger.info(f"✅ Driver initialized: {base_url}")
        
        yield drv

    finally:
        if drv:
            drv.quit()
            logger.info("✅ Driver closed")


# ============================
#  SCREENSHOT ON FAILURE
# ============================
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Take screenshot on test failure"""
    outcome = yield
    result = outcome.get_result()

    if result.when == "call" and result.outcome == "failed":
        try:
            if hasattr(item, 'funcargs') and 'web_driver' in item.funcargs:
                web_driver = item.funcargs['web_driver']
                screenshot_dir = os.path.join(
                    os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
                    "screenshots"
                )
                os.makedirs(screenshot_dir, exist_ok=True)

                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                screenshot_path = os.path.join(
                    screenshot_dir,
                    f"{item.name}_{timestamp}.png"
                )
                web_driver.save_screenshot(screenshot_path)
                logger.error(f"Screenshot saved: {screenshot_path}")
        except Exception as e:
            logger.warning(f"Could not take screenshot: {e}")
