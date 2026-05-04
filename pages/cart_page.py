from pages.base_page import Page
from selenium.webdriver.common.by import By


class CartPage(Page):
    EMPTY_CART_MESSAGE = (By.XPATH, "//*[contains(text(), 'Your cart is empty')]")
    CART_ITEM_TEXT = (By.XPATH,
                      "//*[contains(text(), 'item') or contains(text(), 'Subtotal') or contains(text(), 'Total')]")

    def verify_empty_cart_message(self):
        actual_text = self.find_element(*self.EMPTY_CART_MESSAGE).text
        assert "Your cart is empty" in actual_text, f'Expected empty cart message, but got "{actual_text}"'

    def verify_product_in_cart(self):
        self.open_url("cart")

        cart_items = self.find_elements(*self.CART_ITEM_TEXT)
        print("Cart-related elements found:", len(cart_items))

        assert len(cart_items) > 0

