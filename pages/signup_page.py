from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage

class SignupPage(BasePage):
    # --- Locators ---
    SIGNUP_LOGIN_BTN = (By.XPATH, "//a[@href='/login']")
    
    # Initial Signup
    NAME_INPUT = (By.CSS_SELECTOR, "input[data-qa='signup-name']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[data-qa='signup-email']")
    SIGNUP_BTN = (By.CSS_SELECTOR, "button[data-qa='signup-button']")
    
    # Form Fields
    TITLE_MR = (By.ID, "id_gender1")
    PASSWORD_FIELD = (By.ID, "password")
    DAY_DROPDOWN = (By.ID, "days")
    MONTH_DROPDOWN = (By.ID, "months")
    YEAR_DROPDOWN = (By.ID, "years")
    
    FIRST_NAME = (By.ID, "first_name")
    LAST_NAME = (By.ID, "last_name")
    ADDRESS = (By.ID, "address1")
    COUNTRY_DROPDOWN = (By.ID, "country")
    STATE = (By.ID, "state")
    CITY = (By.ID, "city")
    ZIPCODE = (By.ID, "zipcode")
    MOBILE = (By.ID, "mobile_number")
    
    CREATE_ACCOUNT_BTN = (By.CSS_SELECTOR, "button[data-qa='create-account']")
    
    # Validation Messages
    ACCOUNT_CREATED_MSG = (By.XPATH, "//b[text()='Account Created!']")
    CONTINUE_BTN = (By.CSS_SELECTOR, "a[data-qa='continue-button']")
    
    DELETE_ACCOUNT_BTN = (By.CSS_SELECTOR, "a[href='/delete_account']")
    ACCOUNT_DELETED_MSG = (By.XPATH, "//b[text()='Account Deleted!']")

    # --- Actions ---
    def click_signup_login(self):
        self.click(self.SIGNUP_LOGIN_BTN)

    def fill_initial_signup(self, name, email):
        self.send_keys(self.NAME_INPUT, name)
        self.send_keys(self.EMAIL_INPUT, email)
        self.click(self.SIGNUP_BTN)

    def fill_details_and_create_account(self, password, fname, lname, address, state, city, zip_code, mobile):
        # 1. Select Title (Mr.)
        self.click(self.TITLE_MR)
        
        # 2. Password
        self.send_keys(self.PASSWORD_FIELD, password)
        
        # 3. Dropdowns (Date of Birth) - Helper function use karenge
        self.select_from_dropdown(self.DAY_DROPDOWN, "10")
        self.select_from_dropdown(self.MONTH_DROPDOWN, "May")
        self.select_from_dropdown(self.YEAR_DROPDOWN, "2000")
        
        # 4. Address Details
        self.send_keys(self.FIRST_NAME, fname)
        self.send_keys(self.LAST_NAME, lname)
        self.send_keys(self.ADDRESS, address)
        self.select_from_dropdown(self.COUNTRY_DROPDOWN, "India")
        self.send_keys(self.STATE, state)
        self.send_keys(self.CITY, city)
        self.send_keys(self.ZIPCODE, zip_code)
        self.send_keys(self.MOBILE, mobile)
        
        # 5. Click Create
        self.click(self.CREATE_ACCOUNT_BTN)

    def is_account_created(self):
        try:
            return self.find_element(self.ACCOUNT_CREATED_MSG).is_displayed()
        except:
            return False

    def click_continue(self):
        self.click(self.CONTINUE_BTN)

    def delete_account(self):
        self.click(self.DELETE_ACCOUNT_BTN)

    def is_account_deleted(self):
        try:
            return self.find_element(self.ACCOUNT_DELETED_MSG).is_displayed()
        except:
            return False

    # --- Helper for Dropdown ---
    def select_from_dropdown(self, locator, visible_text):
        dropdown_element = self.find_element(locator)
        select = Select(dropdown_element)
        select.select_by_visible_text(visible_text)