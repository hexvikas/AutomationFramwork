from selenium.webdriver.common.by import By
from core.base_page import BasePage

class ProductsPage(BasePage):
    # Locators
    PRODUCTS_NAV_BTN = (By.XPATH, "//a[@href='/products']")
    SEARCH_BOX = (By.ID, "search_product")
    SEARCH_BTN = (By.ID, "submit_search")
    
    # Buttons
    VIEW_PRODUCT_BTN = (By.XPATH, "(//a[contains(text(),'View Product')])[1]")
    FIRST_PRODUCT_ADD_BTN = (By.XPATH, "(//a[contains(text(),'Add to cart')])[1]")
    
    # Detail Page
    QUANTITY_INPUT = (By.ID, "quantity")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "button.cart")
    
    CONTINUE_SHOPPING_BTN = (By.XPATH, "//button[text()='Continue Shopping']")
    CART_NAV_BTN = (By.XPATH, "//a[@href='/view_cart']")

    # Actions
    def click_products_nav(self):
        self.click(self.PRODUCTS_NAV_BTN)

    def search_product(self, product_name):
        self.send_keys(self.SEARCH_BOX, product_name)
        self.click(self.SEARCH_BTN)

    def add_first_product_to_cart(self):
        self.force_click(self.FIRST_PRODUCT_ADD_BTN)

    # UPDATED: Use force_click for View Product to bypass Ads
    def view_first_product(self):
        self.force_click(self.VIEW_PRODUCT_BTN)

    def set_quantity(self, qty):
        self.send_keys(self.QUANTITY_INPUT, str(qty))

    def add_to_cart(self):
        self.force_click(self.ADD_TO_CART_BTN)

    def click_continue_shopping(self):
        self.force_click(self.CONTINUE_SHOPPING_BTN)

    def go_to_cart(self):
        self.click(self.CART_NAV_BTN)