import allure
from selenium.webdriver.common.by import By
from core.base_page import BasePage


class LoginPage(BasePage):

    # -------------------------------
    # Locators
    # -------------------------------
    EMAIL_FIELD = (By.CSS_SELECTOR, "input[data-qa='login-email']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "input[data-qa='login-password']")
    LOGIN_BTN = (By.CSS_SELECTOR, "button[data-qa='login-button']")
    LOGOUT_BTN = (By.CSS_SELECTOR, "a[href='/logout']")
    ERROR_MSG = (By.CSS_SELECTOR, ".login-form p")  # Optional invalid error

    # -------------------------------
    # Constructor
    # -------------------------------
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://automationexercise.com/login"

    # -------------------------------
    # Page Actions
    # -------------------------------
    @allure.step("Open Login Page")
    def load(self):
        self.driver.get(self.url)

    @allure.step("Perform login with email: {1}")
    def login(self, email, password):
        self.wait_until_visible(self.EMAIL_FIELD)
        self.send_keys(self.EMAIL_FIELD, email)
        self.send_keys(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BTN)

    @allure.step("Check if logout button is visible")
    def is_logged_in(self):
        """Better version of the old is_logout_displayed()"""
        try:
            return self.wait_until_visible(self.LOGOUT_BTN)
        except:
            return False

    @allure.step("Click logout button")
    def logout(self):
        try:
            element = self.wait_until_visible(self.LOGOUT_BTN)
            element.click()
        except:
            pass  # No logout available → ignore
