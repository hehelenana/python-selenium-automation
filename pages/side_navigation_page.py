from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.base_page import Page


class SideNavigationPage(Page):
    SIGN_IN_BUTTON = (By.XPATH, "//button[contains(text(), 'Sign in or create account')]")

    def click_sign_in(self):
        sign_in_button = self.find_element(*self.SIGN_IN_BUTTON)
        sign_in_button.send_keys(Keys.ENTER)