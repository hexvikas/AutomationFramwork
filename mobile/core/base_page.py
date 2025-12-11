import time
import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    StaleElementReferenceException,
    NoSuchElementException
)


class MobileBasePage:
    """Base class for Mobile Pages (Appium-based)"""

    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.timeout = timeout

    # ==================== FIND METHODS ====================
    def find(self, locator):
        """Find element with presence check"""
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_visible(self, locator):
        """Find visible element"""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_all(self, locator):
        """Find multiple elements"""
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    # ==================== CLICK METHODS ====================
    def click(self, locator):
        """Click on element"""
        try:
            element = self.find_visible(locator)
            element.click()
        except StaleElementReferenceException:
            time.sleep(0.5)
            self.find(locator).click()

    def log_and_click(self, locator, message=""):
        """Click with logging"""
        self.click(locator)
        if message:
            allure.step(message)

    # ==================== TEXT INPUT ====================
    def type_text(self, locator, text):
        """Type text in field"""
        element = self.find_visible(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """Get element text"""
        return self.find(locator).text

    # ==================== WAIT & VISIBILITY ====================
    def wait_until_visible(self, locator):
        """Wait until element is visible"""
        return self.find_visible(locator)

    def is_element_visible(self, locator):
        """Check if element is visible"""
        try:
            return self.find_visible(locator).is_displayed()
        except TimeoutException:
            return False

    def is_element_present(self, locator):
        """Check if element exists"""
        try:
            self.find(locator)
            return True
        except (TimeoutException, NoSuchElementException):
            return False

    # ==================== DEVICE ACTIONS ====================
    def take_screenshot(self, filename):
        """Take screenshot"""
        self.driver.save_screenshot(filename)

    def swipe_up(self):
        """Swipe up"""
        size = self.driver.get_window_size()
        self.driver.swipe(size['width']//2, size['height']*0.7,
                         size['width']//2, size['height']*0.3)

    def swipe_down(self):
        """Swipe down"""
        size = self.driver.get_window_size()
        self.driver.swipe(size['width']//2, size['height']*0.3,
                         size['width']//2, size['height']*0.7)
