import pytest
from pages.signup_page import SignupPage
from utilities.custom_logger import LogGen
from utilities.random_utils import generate_random_email

class TestSignup:
    def test_register_user(self, driver):
        logger = LogGen.loggen()
        logger.info("***** Starting TC_01: Register User Test *****")
        
        # 1. Generate Unique Data
        random_email = generate_random_email()
        name = "Automation Hero"
        logger.info(f"Using Email: {random_email}")
        
        signup_page = SignupPage(driver)
        
        # 2. Open Application URL
        signup_page.load()
        logger.info("Application URL Loaded")
        
        # 3. Start Signup Flow
        signup_page.click_signup_login()
        signup_page.fill_initial_signup(name, random_email)
        logger.info("Initial details filled")
        
        # 4. Fill Registration Form
        signup_page.fill_details_and_create_account(
            "Pass123", "Test", "User", "123 Tech Park", "Gujarat", "Ahmedabad", "380001", "9876543210"
        )
        logger.info("Registration form filled")
        
        # 5. Verify Account Creation
        if signup_page.is_account_created():
            logger.info("[PASS] Account Created Successfully")
        else:
            logger.error("[FAIL] Account Creation Failed")
            driver.save_screenshot("reports/signup_fail.png")
            assert False
            
        # 6. Cleanup: Delete the account
        signup_page.click_continue()
        signup_page.delete_account()
        
        if signup_page.is_account_deleted():
            logger.info("[PASS] Account Deleted Successfully")
            assert True
        else:
            logger.error("[FAIL] Account Delete Failed")
            assert False