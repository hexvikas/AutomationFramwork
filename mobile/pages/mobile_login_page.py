from appium.webdriver.common.appiumby import AppiumBy
from mobile.utils.mobile_utils import MobileUtils
from mobile.core.base_page import MobileBasePage

class MobileLoginPage(MobileBasePage):

    EMAIL = (AppiumBy.XPATH, "//input[@type='email']")
    PASSWORD = (AppiumBy.XPATH, "//input[@type='password']")
    LOGIN_BTN = (AppiumBy.XPATH, "//button[text()='Login']")

    def __init__(self, driver):
        super().__init__(driver)
        self.mobile = MobileUtils(driver)

    def login(self, email, password):
        self.type_text(self.EMAIL, email)
        self.type_text(self.PASSWORD, password)

        self.mobile.hide_keyboard()
        self.log_and_click(self.LOGIN_BTN, "Logging in")
