from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductsPage(BasePage):
    # ... (Keep existing locators exactly same) ...
    PRODUCTS_NAV_BTN = (By.XPATH, "//a[@href='/products']")
    SEARCH_BOX = (By.ID, "search_product")
    SEARCH_BTN = (By.ID, "submit_search")
    FIRST_PRODUCT_ADD_BTN = (By.XPATH, "(//a[contains(text(),'Add to cart')])[1]")
    CONTINUE_SHOPPING_BTN = (By.XPATH, "//button[text()='Continue Shopping']")
    CART_NAV_BTN = (By.XPATH, "//a[@href='/view_cart']")

    def click_products_nav(self):
        self.click(self.PRODUCTS_NAV_BTN)

    def search_product(self, product_name):
        self.send_keys(self.SEARCH_BOX, product_name)
        self.click(self.SEARCH_BTN)

    def add_first_product_to_cart(self):
        # UPDATE: Use force_click here to bypass Ads
        self.force_click(self.FIRST_PRODUCT_ADD_BTN)
        
    def click_continue_shopping(self):
        # Isme bhi zarurat pad sakti hai
        self.force_click(self.CONTINUE_SHOPPING_BTN)
        
    def go_to_cart(self):
        self.click(self.CART_NAV_BTN)