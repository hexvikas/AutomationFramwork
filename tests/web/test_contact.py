import pytest
import os
from pages.contact_page import ContactPage
from utilities.custom_logger import LogGen

class TestContactForm:
    def test_contact_us_upload(self, driver):
        logger = LogGen.loggen()
        logger.info("***** Starting TC: Contact Us Form *****")
        
        contact = ContactPage(driver)
        
        # 1. Dummy File Create Karo (Upload ke liye)
        file_path = os.path.join(os.getcwd(), "test_upload.txt")
        with open(file_path, "w") as f:
            f.write("This is a test file for automation.")
            
        # 2. Navigate to Contact Page 
        driver.get("https://automationexercise.com") 
        contact.click_contact_us()
        logger.info("Opened Contact Page")
        
        # 3. Form fillup
        contact.fill_form("Test User", "test@test.com", "Subject Here", "Message Here", file_path)
        logger.info("Form Filled & File Uploaded")
        
        # 4. Submit 
        contact.submit_form()
        logger.info("Form Submitted")
        
        # 5. Verify Success
        msg = contact.get_success_msg()
        if "Success! Your details have been submitted" in msg:
            logger.info("[PASS] Contact Form Verified")
            assert True
        else:
            logger.error(f"[FAIL] Message mismatch: {msg}")
            driver.save_screenshot("reports/contact_fail.png")
            assert False
            
        # Cleanup (Dummy files detelete )
        if os.path.exists(file_path):
            os.remove(file_path)