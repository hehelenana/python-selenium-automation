from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Header(Page):
    SEARCH_FIELD = (By.ID, "search")
    CART_ICON = (By.CSS_SELECTOR, "a[data-test='@web/CartLink']")
    ACCOUNT_BUTTON = (By.CSS_SELECTOR, "[data-test='@web/AccountLink']")

    def search_product(self, search_query):
        self.input_text(search_query, *self.SEARCH_FIELD)
        self.find_element(*self.SEARCH_FIELD).send_keys(Keys.ENTER)

    def click_cart_icon(self):
        self.click(*self.CART_ICON)

    def click_account(self):
        self.click(*self.ACCOUNT_BUTTON)