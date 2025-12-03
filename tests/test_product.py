import pytest
import time
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from utilities.read_config import ReadConfig
from utilities.custom_logger import LogGen

class TestProductFlow:
    # Config se URL aur Data uthao
    user = "correct_user@test.com" # Replace with valid email
    pwd = "correct_pass"           # Replace with valid password
    product_name = "Tshirt"

    def test_search_and_add_to_cart(self, driver):
        logger = LogGen.loggen()
        logger.info("***** Starting Product Search & Add to Cart Test *****")
        
        # 1. Login
        login_page = LoginPage(driver)
        login_page.load()
        login_page.login(self.user, self.pwd)
        logger.info("Login Successful")

        # 2. Go to Products
        prod_page = ProductsPage(driver)
        prod_page.click_products_nav()
        logger.info("Navigated to Products Page")

        # 3. Search
        prod_page.search_product(self.product_name)
        logger.info(f"Searched for: {self.product_name}")

        # 4. Add to Cart
        try:
            prod_page.add_first_product_to_cart()
            logger.info("Clicked Add to Cart")
            time.sleep(2)
            prod_page.click_continue_shopping()
            logger.info("Popup handled.")
        except Exception as e:
            logger.error(f"Failed to add to cart: {e}")
            assert False

        # 5. Verify Cart
        prod_page.go_to_cart()
        if "view_cart" in driver.current_url:
            logger.info("[PASS] Reached Cart Page")
            assert True
        else:
            logger.error("[FAIL] Cart Page not reached")
            assert False