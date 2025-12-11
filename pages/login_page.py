from selenium.webdriver.common.by import By
from core.base_page import BasePage


class LoginPage(BasePage):
    # Locators (your original selectors — correct!)
    EMAIL_FIELD = (By.CSS_SELECTOR, "input[data-qa='login-email']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "input[data-qa='login-password']")
    LOGIN_BTN = (By.CSS_SELECTOR, "button[data-qa='login-button']")
    LOGOUT_BTN = (By.CSS_SELECTOR, "a[href='/logout']")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://automationexercise.com/login"

    def load(self):
        """Open the Login page."""
        self.driver.get(self.url)

    def login(self, email, password):
        """Perform login."""
        self.send_keys(self.EMAIL_FIELD, email)
        self.send_keys(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BTN)

    def is_logout_displayed(self):
        """Check logout link visibility."""
        try:
            return self.find(self.LOGOUT_BTN).is_displayed()
        except Exception:
            return False
