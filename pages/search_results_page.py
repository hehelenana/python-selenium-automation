from pages.base_page import Page
from selenium.webdriver.common.by import By


class SearchResultsPage(Page):
    SEARCH_RESULT_TEXT = (By.XPATH, "//div[contains(@class, 'styles_resultCount')]")
    ADD_TO_CART_BUTTONS = (By.XPATH, "//button[contains(@aria-label, 'Add') and contains(@aria-label, 'to cart')]")

    def verify_search_results(self, product):
        actual_result = self.find_element(*self.SEARCH_RESULT_TEXT).text
        assert product in actual_result, f'Expected "{product}" not in actual "{actual_result}"'

    def add_first_product_to_cart(self):
        add_buttons = self.find_elements(*self.ADD_TO_CART_BUTTONS)
        print("Add to cart buttons found:", len(add_buttons))

        add_button = self.find_element(
            By.XPATH,
            "(//button[contains(@aria-label, 'Add') and contains(@aria-label, 'to cart')])[2]"
        )

        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", add_button)
        self.driver.execute_script("arguments[0].click();", add_button)

