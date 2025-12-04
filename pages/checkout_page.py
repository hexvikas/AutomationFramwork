from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    # --- Locators ---
    COMMENT_AREA = (By.NAME, "message")
    PLACE_ORDER_BTN = (By.XPATH, "//a[@href='/payment']")

    # --- Actions ---
    def enter_comment(self, text):
        self.send_keys(self.COMMENT_AREA, text)

    def click_place_order(self):
        # Using force_click to avoid ads/overlays overlapping the button
        self.force_click(self.PLACE_ORDER_BTN)
