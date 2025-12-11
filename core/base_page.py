import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    StaleElementReferenceException,
    ElementClickInterceptedException
)

class BasePage:

    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    # -----------------------------
    # GENERIC FIND ELEMENT
    # -----------------------------
    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    # -----------------------------
    #  CLICK METHODS
    # -----------------------------
    def click(self, locator):
        try:
            element = self.find_visible(locator)
            element.click()
        except (StaleElementReferenceException, ElementClickInterceptedException):
            time.sleep(1)
            self.force_click(locator)

    def force_click(self, locator):
        element = self.find(locator)
        self.driver.execute_script("arguments[0].click();", element)

    # -----------------------------
    #  SEND KEYS METHODS
    # -----------------------------
    def send_keys(self, locator, text):
        element = self.find_visible(locator)
        element.clear()
        element.send_keys(text)

    def js_send_keys(self, locator, text):
        element = self.find(locator)
        self.driver.execute_script("arguments[0].value = arguments[1];", element, text)

    # -----------------------------
    #  GET TEXT METHODS
    # -----------------------------
    def get_text(self, locator):
        element = self.find_visible(locator)
        return element.text

    # -----------------------------
    #  WAIT HELPERS
    # -----------------------------
    def wait_until_visible(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_until_clickable(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    # -----------------------------
    #  SCROLL (WEB + MOBILE)
    # -----------------------------
    def scroll_to_element(self, locator):
        element = self.find(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        return element

    def scroll_down(self, px=400):
        self.driver.execute_script(f"window.scrollBy(0, {px});")

    # -----------------------------
    #  ALLURE SCREENSHOT
    # -----------------------------
    def take_screenshot(self, name="screenshot"):
        screenshot = self.driver.get_screenshot_as_png()
        allure.attach(screenshot, name=name, attachment_type=allure.attachment_type.PNG)

    # -----------------------------
    #  SAFE ACTION WRAPPER
    # -----------------------------
    def safe_action(self, func, locator, retries=2):
        for attempt in range(retries):
            try:
                return func(locator)
            except Exception as e:
                if attempt == retries - 1:
                    self.take_screenshot("failure")
                    raise e
                time.sleep(1)
