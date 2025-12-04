import pytest
import os
import allure
from pages.login_page import LoginPage
from utilities.excel_utils import get_data_from_excel
from utilities.custom_logger import LogGen

data_path = "test_data/login_data.xlsx"
sheet_name = "Sheet1"
test_data = get_data_from_excel(data_path, sheet_name)

# UPDATE: Added 'description' variable to handle the 4th column in Excel
@pytest.mark.parametrize("email, password, res_type, description", test_data)
def test_login_ddt(driver, email, password, res_type, description):
    logger = LogGen.loggen()
    run_id = os.environ.get("CURRENT_RUN_ID")
    
    logger.info(f"*** Starting Test: {email} | Type: {res_type} ***")
    
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login(email, password)
    
    is_logged_in = login_page.is_logout_displayed()
    
    if res_type == "Valid":
        if is_logged_in:
            logger.info("[PASS] Login Successful")
            driver.find_element_by_xpath("//a[@href='/logout']").click()
            assert True
        else:
            logger.error("[FAIL] Login Failed")
            driver.save_screenshot(f"reports/Error_ID{run_id}_valid_fail.png")
            assert False

    elif res_type == "Invalid":
        if is_logged_in:
            logger.error("[FAIL] Invalid Login worked unexpectedly")
            driver.find_element_by_xpath("//a[@href='/logout']").click()
            assert False
        else:
            logger.info("[PASS] Login Failed as expected")
            assert True