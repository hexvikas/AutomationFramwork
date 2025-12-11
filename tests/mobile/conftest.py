import pytest
import os
from datetime import datetime

from utilities.custom_logger import LogGen
from mobile.core.appium_driver import AppiumDriver

logger = LogGen.loggen()


@pytest.fixture(scope="function")
def mobile_driver(request):
    """Mobile driver fixture for Appium tests"""
    platform = request.config.getoption("--platform", default="android").lower()
    
    try:
        driver_manager = AppiumDriver(platform=platform)
        drv = driver_manager.get_driver()
        logger.info(f"✅ Mobile driver initialized: {platform}")
        
        yield drv

    finally:
        if drv:
            drv.quit()
            logger.info("✅ Mobile driver closed")


# ============================
#  SCREENSHOT ON FAILURE
# ============================
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Take screenshot on mobile test failure"""
    outcome = yield
    result = outcome.get_result()

    if result.when == "call" and result.outcome == "failed":
        try:
            if hasattr(item, 'funcargs') and 'mobile_driver' in item.funcargs:
                mobile_driver = item.funcargs['mobile_driver']
                screenshot_dir = os.path.join(
                    os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
                    "screenshots"
                )
                os.makedirs(screenshot_dir, exist_ok=True)

                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                screenshot_path = os.path.join(
                    screenshot_dir,
                    f"{item.name}_mobile_{timestamp}.png"
                )
                mobile_driver.save_screenshot(screenshot_path)
                logger.error(f"Screenshot saved: {screenshot_path}")
        except Exception as e:
            logger.warning(f"Could not take screenshot: {e}")


def pytest_addoption(parser):
    """Add --platform option for mobile tests"""
    parser.addoption(
        "--platform",
        action="store",
        default="android",
        help="Choose platform: android or ios"
    )
