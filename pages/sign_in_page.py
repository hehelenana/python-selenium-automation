from selenium.webdriver.common.by import By

from pages.base_page import Page


class SignInPage(Page):
    SIGN_IN_FORM_TEXT = (By.XPATH, "//*[contains(text(), 'Sign in or create account')]")
    SIGN_IN_BUTTON = (By.XPATH, "//button[contains(text(), 'Sign in')]")

    def verify_sign_in_form_opened(self):
        self.find_element(*self.SIGN_IN_FORM_TEXT)
        self.find_element(*self.SIGN_IN_BUTTON)