import pytest
import time
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from utilities.read_config import ReadConfig
from utilities.custom_logger import LogGen

class TestProductFlow:
    # Config se URL aur Data uthao (Hardcoded for now purely for functional test)
    user = "correct_user@test.com" # Replace with your valid email
    pwd = "correct_pass"           # Replace with your valid password
    product_name = "Tshirt"

    logger = LogGen.loggen()

    def test_search_and_add_to_cart(self, driver):
        self.logger.info("***** Starting Product Search & Add to Cart Test *****")
        
        # 1. Login  (Reuse LoginPage)
        login_page = LoginPage(driver)
        login_page.load()
        login_page.login(self.user, self.pwd)
        self.logger.info("Login Successful")

        # 2. Navigate to Products
        prod_page = ProductsPage(driver)
        prod_page.click_products_nav()
        self.logger.info("Navigated to Products Page")

        # 3. Searching product
        prod_page.search_product(self.product_name)
        self.logger.info(f"Searched for: {self.product_name}")

        # 4. Add to Cart waiting for popup
        # Note: Site sometimes fails to add to cart, so try-except added
        try:
            prod_page.add_first_product_to_cart()
            self.logger.info("Clicked Add to Cart")
            
            # waiting for popup and handling
            time.sleep(2) #Small wait for popup
            prod_page.click_continue_shopping()
            self.logger.info("Product added. Popup handled.")
            
        except Exception as e:
            self.logger.error(f"Failed to add to cart: {e}")
            driver.save_screenshot("reports/cart_error.png")
            assert False

        # 5. Verify in Cart
        prod_page.go_to_cart()
        self.logger.info("Navigated to Cart Page")
        
        # Simple verification: Check if URL contains 'view_cart'
        if "view_cart" in driver.current_url:
            self.logger.info("[PASS] Successfully reached Cart Page")
            assert True
        else:
            self.logger.error("[FAIL] Could not reach Cart Page")
            assert False