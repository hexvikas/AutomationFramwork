import pytest
from pages.signup_page import SignupPage
from utilities.custom_logger import LogGen
from utilities.random_utils import generate_random_email

class TestSignup:
    
    def test_register_user(self, driver):
        logger = LogGen.loggen()
        logger.info("***** Starting TC_01: Register User Test *****")
        
        # 1. Generate Random Data
        random_email = generate_random_email()
        name = "Automation Hero"
        logger.info(f"Using Email: {random_email}")
        
        signup_page = SignupPage(driver)
        
        # 2. Navigate to Signup
        signup_page.click_signup_login()
        logger.info("Clicked Signup/Login button")
        
        # 3. Fill Initial Info
        signup_page.fill_initial_signup(name, random_email)
        logger.info("Filled initial signup details")
        
        # 4. Fill Detailed Form
        logger.info("Filling Account Information form...")
        signup_page.fill_details_and_create_account(
            password="Password123",
            fname="Test",
            lname="User",
            address="123 Street, Tech Park",
            state="Gujarat",
            city="Ahmedabad",
            zip_code="380001",
            mobile="9876543210"
        )
        
        # 5. Verify Account Created
        if signup_page.is_account_created():
            logger.info("[PASS] Account Created Successfully")
        else:
            logger.error("[FAIL] Account Creation Failed")
            driver.save_screenshot("reports/signup_fail.png")
            assert False
            
        # 6. Click Continue & Delete Account (Cleanup)
        signup_page.click_continue()
        logger.info("Clicked Continue")
        
        signup_page.delete_account()
        logger.info("Clicked Delete Account")
        
        if signup_page.is_account_deleted():
            logger.info("[PASS] Account Deleted Successfully")
            assert True
        else:
            logger.error("[FAIL] Account Delete Failed")
            assert False