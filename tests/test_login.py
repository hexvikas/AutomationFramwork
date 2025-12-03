import pytest
import os
import allure
from pages.login_page import LoginPage
from utilities.excel_utils import get_data_from_excel
from utilities.custom_logger import LogGen

data_path = "test_data/login_data.xlsx"
sheet_name = "Sheet1"
test_data = get_data_from_excel(data_path, sheet_name)

@pytest.mark.parametrize("email, password, res_type", test_data)
def test_login_ddt(driver, email, password, res_type):
    # Logger Init
    logger = LogGen.loggen()
    run_id = os.environ.get("CURRENT_RUN_ID")
    
    logger.info(f"*** Starting Test for: {email} | Expected: {res_type} ***")
    
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login(email, password)
    
    # --- LOGIC START ---
    
    # 1. Check if Login was successful (Logout button visible)
    is_logged_in = login_page.is_logout_displayed()
    
    # SCENARIO A: Expected VALID Login (Correct User/Pass)
    if res_type == "Valid":
        if is_logged_in:
            logger.info("[PASS] Login Successful as expected")
            # Logout zaroori hai taaki agla test fresh start ho sake
            driver.find_element_by_xpath("//a[@href='/logout']").click()
            assert True
        else:
            logger.error("[FAIL] Expected Login Success, but failed")
            capture_screenshot(driver, run_id, "Valid_Login_Fail")
            assert False

    # SCENARIO B: Expected INVALID Login (Wrong User/Pass)
    elif res_type == "Invalid":
        if is_logged_in:
            # Ye fail hai kyunki galat password se login nahi hona chahiye tha!
            logger.error("[FAIL] Login happened with Invalid Data!")
            driver.find_element_by_xpath("//a[@href='/logout']").click()
            capture_screenshot(driver, run_id, "Invalid_Login_Passed_Mistake")
            assert False
        else:
            logger.info("[PASS] Login Failed as expected (Security Check Passed)")
            assert True

def capture_screenshot(driver, run_id, name):
    if not os.path.exists("reports"):
        os.makedirs("reports")
    screenshot_name = f"Error_ID{run_id}_{name}.png"
    driver.save_screenshot(os.path.join("reports", screenshot_name))