import time

from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@given("I open Target website for HW4")
def open_target_website_hw4(context):
    context.driver.get("https://www.target.com/")
    time.sleep(3)


@when('I search for "{product}" for HW4')
def search_for_product_hw4(context, product):
    search_box = context.driver.find_element(By.ID, "search")
    search_box.clear()
    search_box.send_keys(product)
    search_box.send_keys(Keys.ENTER)
    time.sleep(3)


@then('I should see search results for "{product}" for HW4')
def verify_search_results_hw4(context, product):
    search_text = context.driver.find_element(By.XPATH, f"//*[contains(text(), '{product}')]")
    print(search_text.text)


@given("I open Target Circle page for HW4")
def open_target_circle_page_hw4(context):
    context.driver.get("https://www.target.com/circle")
    time.sleep(3)


@then("I should see 2 storycards under Unlock added value for HW4")
def verify_storycards_hw4(context):
    storycards = context.driver.find_elements(
        By.XPATH,
        "//*[contains(text(), 'Unlock added value')]/following::a[contains(@href, '/circle')]"
    )
    print(len(storycards))


@when("I add the first product to the cart for HW4")
def add_first_product_to_cart_hw4(context):
    add_buttons = context.driver.find_elements(
        By.XPATH,
        "//button[contains(@aria-label, 'Add') and contains(@aria-label, 'to cart')]"
    )
    print(len(add_buttons))

    add_buttons[1].send_keys(Keys.ENTER)
    time.sleep(3)


@then("I should see the product in the cart for HW4")
def verify_product_in_cart_hw4(context):
    context.driver.get("https://www.target.com/cart")
    time.sleep(3)

    cart_items = context.driver.find_elements(
        By.XPATH,
        "//*[contains(text(), 'item') or contains(text(), 'Subtotal') or contains(text(), 'Total')]"
    )
    print(len(cart_items))