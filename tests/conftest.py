import pytest
import os
from datetime import datetime

from utilities.read_config import ReadConfig
from utilities.custom_logger import LogGen

logger = LogGen.loggen()


# ============================
#  GLOBAL CLI OPTIONS
# ============================
def pytest_addoption(parser):
    parser.addoption(
        "--platform",
        action="store",
        default="web",
        help="Choose platform: web, android, or ios"
    )


# ============================
#  DEPRECATED: Use platform-specific conftest instead
# ============================
# Web tests: Use fixture 'web_driver' from tests/web/conftest.py
# Mobile tests: Use fixture 'mobile_driver' from tests/mobile/conftest.py
# API tests: Use fixture 'api_client' from tests/api/conftest.py


# ============================
#  SCREENSHOT ON FAILURE
# ============================
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    result = outcome.get_result()

    if result.when == "call" and result.failed:

        driver = item.funcargs.get("driver", None)

        if driver:
            try:
                os.makedirs("screenshots", exist_ok=True)

                ts = datetime.now().strftime("%Y%m%d_%H%M%S")
                file_path = f"screenshots/{item.name}_{ts}.png"

                driver.save_screenshot(file_path)
                print(f"\n📸 Screenshot Saved: {file_path}")

            except Exception as e:
                print(f"\n⚠️ Screenshot capture failed: {e}")
