from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from core.base_page import BasePage
from utilities.read_config import ReadConfig

class SignupPage(BasePage):
    # --- Locators ---
    SIGNUP_LOGIN_BTN = (By.XPATH, "//a[@href='/login']")
    NAME_INPUT = (By.CSS_SELECTOR, "input[data-qa='signup-name']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[data-qa='signup-email']")
    SIGNUP_BTN = (By.CSS_SELECTOR, "button[data-qa='signup-button']")
    
    TITLE_MR = (By.ID, "id_gender1")
    PASSWORD_FIELD = (By.ID, "password")
    DAY = (By.ID, "days")
    MONTH = (By.ID, "months")
    YEAR = (By.ID, "years")
    
    FNAME = (By.ID, "first_name")
    LNAME = (By.ID, "last_name")
    ADDRESS = (By.ID, "address1")
    COUNTRY = (By.ID, "country")
    STATE = (By.ID, "state")
    CITY = (By.ID, "city")
    ZIP = (By.ID, "zipcode")
    MOBILE = (By.ID, "mobile_number")
    
    CREATE_ACCOUNT_BTN = (By.CSS_SELECTOR, "button[data-qa='create-account']")
    ACCOUNT_CREATED_MSG = (By.XPATH, "//b[text()='Account Created!']")
    CONTINUE_BTN = (By.CSS_SELECTOR, "a[data-qa='continue-button']")
    DELETE_ACCOUNT_BTN = (By.CSS_SELECTOR, "a[href='/delete_account']")
    ACCOUNT_DELETED_MSG = (By.XPATH, "//b[text()='Account Deleted!']")

    def __init__(self, driver):
        super().__init__(driver)
        base_url = ReadConfig.get_application_url()
        # Ensure we land on Home Page, not directly on login
        self.url = base_url.replace("/login", "") 

    def load(self):
        self.driver.get(self.url)

    def click_signup_login(self):
        # UPDATED: Use force_click to bypass Ads/Overlays on Home Page
        self.force_click(self.SIGNUP_LOGIN_BTN)

    def fill_initial_signup(self, name, email):
        self.send_keys(self.NAME_INPUT, name)
        self.send_keys(self.EMAIL_INPUT, email)
        self.click(self.SIGNUP_BTN)

    def fill_details_and_create_account(self, password, fname, lname, address, state, city, zip_code, mobile):
        # Wait for the Registration Form to load completely
        self.wait_for_element(self.TITLE_MR)
        
        self.click(self.TITLE_MR)
        self.send_keys(self.PASSWORD_FIELD, password)
        self.select_dropdown(self.DAY, "10")
        self.select_dropdown(self.MONTH, "May")
        self.select_dropdown(self.YEAR, "2000")
        
        self.send_keys(self.FNAME, fname)
        self.send_keys(self.LNAME, lname)
        self.send_keys(self.ADDRESS, address)
        self.select_dropdown(self.COUNTRY, "India")
        self.send_keys(self.STATE, state)
        self.send_keys(self.CITY, city)
        self.send_keys(self.ZIP, zip_code)
        self.send_keys(self.MOBILE, mobile)
        self.click(self.CREATE_ACCOUNT_BTN)

    def is_account_created(self):
        try: return self.find_element(self.ACCOUNT_CREATED_MSG).is_displayed()
        except: return False

    def click_continue(self):
        self.click(self.CONTINUE_BTN)

    def delete_account(self):
        self.click(self.DELETE_ACCOUNT_BTN)

    def is_account_deleted(self):
        try: return self.find_element(self.ACCOUNT_DELETED_MSG).is_displayed()
        except: return False

    def select_dropdown(self, locator, text):
        select = Select(self.find_element(locator))
        select.select_by_visible_text(text)