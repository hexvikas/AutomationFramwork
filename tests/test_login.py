import pytest
import os
import allure
from pages.login_page import LoginPage
from utilities.excel_utils import get_data_from_excel
from utilities.custom_logger import LogGen
from selenium.webdriver.common.by import By

data_path = "test_data/login_data.xlsx"
sheet_name = "Sheet1"
test_data = get_data_from_excel(data_path, sheet_name)


@pytest.mark.parametrize("email, password, res_type, description", test_data)
def test_login_ddt(driver, email, password, res_type, description):
    logger = LogGen.loggen()
    run_id = os.environ.get("CURRENT_RUN_ID")

    logger.info(f"---- Starting Login Test | Email: {email} | Expected: {res_type} ----")

    login_page = LoginPage(driver)
    login_page.load()
    login_page.login(email, password)

    is_logged_in = login_page.is_logout_displayed()

    # ==========================
    # VALID LOGIN CASE
    # ==========================
    if res_type == "Valid":
        if is_logged_in:
            logger.info("[PASS] Valid login succeeded")

            # Proper Selenium 4 locator
            logout_btn = driver.find_element(By.XPATH, "//a[@href='/logout']")
            logout_btn.click()
            assert True

        else:
            logger.error("[FAIL] Expected login success but failed")
            screenshot_path = f"reports/Error_ID{run_id}_valid_fail.png"
            driver.save_screenshot(screenshot_path)
            allure.attach.file(screenshot_path, name="LoginFailure", attachment_type=allure.attachment_type.PNG)
            assert False

    # ==========================
    # INVALID LOGIN CASE
    # ==========================
    elif res_type == "Invalid":
        if is_logged_in:
            logger.error("[FAIL] Invalid login unexpectedly succeeded")
            screenshot_path = f"reports/Error_ID{run_id}_invalid_fail.png"
            driver.save_screenshot(screenshot_path)
            allure.attach.file(screenshot_path, name="UnexpectedLogin", attachment_type=allure.attachment_type.PNG)

            # Click logout to reset state
            logout_btn = driver.find_element(By.XPATH, "//a[@href='/logout']")
            logout_btn.click()
            assert False

        else:
            logger.info("[PASS] Invalid login failed as expected")
            assert True
