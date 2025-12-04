import pytest
import time
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from utilities.custom_logger import LogGen

class TestCartAdvanced:
    
    def test_product_quantity(self, driver):
        logger = LogGen.loggen()
        logger.info("***** TC: Verify Product Quantity *****")
        
        prod = ProductsPage(driver)
        driver.get("https://automationexercise.com") 
        
        prod.view_first_product()
        prod.set_quantity(4)
        prod.add_to_cart()
        time.sleep(2)
        prod.click_continue_shopping()
        prod.go_to_cart()
        
        cart = CartPage(driver)
        if cart.verify_quantity(4):
            logger.info("[PASS] Cart shows Quantity 4")
            assert True
        else:
            logger.error("[FAIL] Quantity Mismatch")
            assert False

    def test_remove_from_cart(self, driver):
        logger = LogGen.loggen()
        logger.info("***** TC: Remove Product From Cart *****")
        
        prod = ProductsPage(driver)
        
        # FIX: URL Load karna zaroori hai!
        driver.get("https://automationexercise.com") 
        
        prod.add_first_product_to_cart()
        time.sleep(2)
        prod.click_continue_shopping()
        prod.go_to_cart()
        
        cart = CartPage(driver)
        initial_count = cart.get_cart_product_count()
        
        if initial_count > 0:
            cart.remove_product()
            logger.info("Clicked Remove Button")
            
            new_count = cart.get_cart_product_count()
            
            if new_count < initial_count:
                logger.info("[PASS] Product Removed Successfully")
                assert True
            else:
                logger.error("[FAIL] Product Not Removed")
                assert False
        else:
             logger.warning("Cart was empty")