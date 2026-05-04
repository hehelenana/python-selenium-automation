from pages.base_page import Page
from selenium.webdriver.common.by import By


class CartPage(Page):
    EMPTY_CART_MESSAGE = (By.XPATH, "//*[contains(text(), 'Your cart is empty')]")

    def verify_empty_cart_message(self):
        actual_text = self.find_element(*self.EMPTY_CART_MESSAGE).text
        assert "Your cart is empty" in actual_text, f'Expected empty cart message, but got "{actual_text}"'