from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class PaymentPage(BasePage):
    # --- Locators ---
    NAME_ON_CARD = (By.NAME, "name_on_card")
    CARD_NUMBER = (By.NAME, "card_number")
    CVC = (By.NAME, "cvc")
    EXPIRY_MONTH = (By.NAME, "expiry_month")
    EXPIRY_YEAR = (By.NAME, "expiry_year")
    PAY_BUTTON = (By.ID, "submit")
    
    # Success Message
    ORDER_PLACED_MSG = (By.XPATH, "//b[text()='Order Placed!']")
    DELETE_ACCOUNT_BTN = (By.XPATH, "//a[@href='/delete_account']")

    # --- Actions ---
    def fill_payment_details(self, name, card_num, cvc, month, year):
        self.send_keys(self.NAME_ON_CARD, name)
        self.send_keys(self.CARD_NUMBER, card_num)
        self.send_keys(self.CVC, cvc)
        self.send_keys(self.EXPIRY_MONTH, month)
        self.send_keys(self.EXPIRY_YEAR, year)

    def click_pay_and_confirm(self):
        # Force click often needed here due to Google Ads
        self.force_click(self.PAY_BUTTON)

    def is_order_placed(self):
        try:
            return self.find_element(self.ORDER_PLACED_MSG).is_displayed()
        except:
            return False
            
    def click_delete_account(self):
        self.force_click(self.DELETE_ACCOUNT_BTN)
