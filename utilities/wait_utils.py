from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    StaleElementReferenceException,
)
import time


class WaitUtils:

    def __init__(self, driver, timeout=10, poll_freq=0.3):
        self.driver = driver
        self.timeout = timeout
        self.poll = poll_freq
        self.wait = WebDriverWait(driver, timeout, poll_frequency=poll_freq,
                                  ignored_exceptions=[StaleElementReferenceException])

    # -----------------------------------------
    # BASIC WAITS
    # -----------------------------------------
    def wait_visible(self, locator):
        """Wait until element becomes visible."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_clickable(self, locator):
        """Wait until element becomes clickable."""
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_presence(self, locator):
        """Wait until element exists in DOM."""
        return self.wait.until(EC.presence_of_element_located(locator))

    # -----------------------------------------
    # SAFE FINDERS
    # -----------------------------------------
    def safe_find(self, locator):
        """Safe way to locate elements without test failing."""
        try:
            return self.wait_presence(locator)
        except TimeoutException:
            return None

    # -----------------------------------------
    # RETRY ELEMENT WAIT
    # -----------------------------------------
    def retry_find(self, locator, attempts=3, delay=0.8):
        """Try to find element with retry logic."""
        for _ in range(attempts):
            el = self.safe_find(locator)
            if el:
                return el
            time.sleep(delay)
        return None
