from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@given("I open Target website for HW3")
def open_target_website_hw3(context):
    context.driver.get("https://www.target.com/")


@when("I click the cart icon for HW3")
def click_cart_icon_hw3(context):
    cart_icon = context.driver.find_element(By.CSS_SELECTOR, "a[data-test='@web/CartLink']")
    cart_icon.click()


@then("I should see the empty cart message for HW3")
def verify_empty_cart_message_hw3(context):
    empty_cart_message = context.driver.find_element(By.XPATH, "//*[contains(text(), 'Your cart is empty')]")
    print(empty_cart_message.text)


@when("I click the account button for HW3")
def click_account_button_hw3(context):
    account_button = context.driver.find_element(By.XPATH, "//span[contains(text(), 'Account')]")
    account_button.click()


@when("I click sign in from the side menu for HW3")
def click_sign_in_from_side_menu_hw3(context):
    sign_in_button = context.driver.find_element(By.XPATH, "//button[contains(text(), 'Sign in or create account')]")
    sign_in_button.send_keys(Keys.ENTER)


@then("I should see the sign in form for HW3")
def verify_sign_in_form_hw3(context):
    sign_in_form_text = context.driver.find_element(By.XPATH, "//*[contains(text(), 'Sign in or create account')]")
    print(sign_in_form_text.text)
