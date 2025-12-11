import pytest
import time
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.payment_page import PaymentPage
from utilities.custom_logger import LogGen

class TestCheckout:
    
    # IMPORTANT: Update this with a valid registered email!
    user = "test_user1_041225@gmail.com" 
    pwd = "Pass123"

    def test_place_order_login_before_checkout(self, driver):
        logger = LogGen.loggen()
        logger.info("***** TC: Place Order: Login before Checkout *****")
        
        # 1. Login
        login = LoginPage(driver)
        driver.get("https://automationexercise.com/login")
        login.login(self.user, self.pwd)
        logger.info("Logged in successfully")
        
        # 2. Add Product to Cart
        prod = ProductsPage(driver)
        prod.click_products_nav()
        prod.add_first_product_to_cart()
        time.sleep(2)
        prod.click_continue_shopping()
        prod.go_to_cart()
        logger.info("Product added to cart")
        
        # 3. Proceed to Checkout
        cart = CartPage(driver)
        cart.click_proceed_to_checkout()
        logger.info("Proceeded to Checkout Page")
        
        # 4. Review Order & Place Order
        checkout = CheckoutPage(driver)
        checkout.enter_comment("Please deliver quickly.")
        checkout.click_place_order()
        logger.info("Order Placed, Navigating to Payment")
        
        # 5. Payment
        pay = PaymentPage(driver)
        pay.fill_payment_details("Test User", "410000000000", "123", "01", "2030")
        pay.click_pay_and_confirm()
        logger.info("Payment Details Submitted")
        
        # 6. Verify Order Placed
        if pay.is_order_placed():
            logger.info("[PASS] Order Placed Successfully!")
            assert True
        else:
            logger.error("[FAIL] Order Placement Failed")
            driver.save_screenshot("reports/order_fail.png")
            assert False
