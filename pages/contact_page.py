from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ContactPage(BasePage):
    CONTACT_LINK = (By.XPATH, "//a[@href='/contact_us']")
    NAME = (By.NAME, "name")
    EMAIL = (By.NAME, "email")
    SUBJECT = (By.NAME, "subject")
    MESSAGE = (By.NAME, "message")
    UPLOAD_FILE = (By.NAME, "upload_file")
    SUBMIT_BTN = (By.NAME, "submit")
    SUCCESS_MSG = (By.CLASS_NAME, "status") 

    def click_contact_us(self):
        self.click(self.CONTACT_LINK)

    def fill_form(self, name, email, subject, message, file_path):
        self.send_keys(self.NAME, name)
        self.send_keys(self.EMAIL, email)
        self.send_keys(self.SUBJECT, subject)
        self.send_keys(self.MESSAGE, message)
        self.send_keys(self.UPLOAD_FILE, file_path)

    def submit_form(self):
        self.click(self.SUBMIT_BTN)
        try:
            self.driver.switch_to.alert.accept()
        except:
            pass

    def get_success_msg(self):
        return self.get_text(self.SUCCESS_MSG)