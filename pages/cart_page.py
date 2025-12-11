from selenium.webdriver.common.by import By
from core.base_page import BasePage
import time

class CartPage(BasePage):
    # Locators
    CART_PRODUCT_ROWS = (By.XPATH, "//tbody/tr")
    CHECKOUT_BTN = (By.CSS_SELECTOR, "a.check_out")
    
    # Delete 'X' button (first product)
    DELETE_BTN = (By.CLASS_NAME, "cart_quantity_delete")
    
    # Modal Link
    MODAL_REGISTER_LOGIN_LINK = (By.XPATH, "//u[text()='Register / Login']")

    # Actions
    def get_cart_product_count(self):
        try:
            rows = self.driver.find_elements(*self.CART_PRODUCT_ROWS)
            return len(rows)
        except:
            return 0

    def verify_quantity(self, expected_qty):
        # In Cart "Quantity" column usually 'disabled' class button
        try:
            qty_element = self.driver.find_element(By.CLASS_NAME, "disabled") 
            actual_qty = qty_element.text
            return actual_qty == str(expected_qty)
        except:
            return False

    def remove_product(self):
        self.click(self.DELETE_BTN)
        time.sleep(2) # To disapper the raw

    def click_proceed_to_checkout(self):
        # CHANGE: Use force_click instead of click to bypass Ads
        self.force_click(self.CHECKOUT_BTN)
        
    def click_modal_register_login(self):
        self.click(self.MODAL_REGISTER_LOGIN_LINK)