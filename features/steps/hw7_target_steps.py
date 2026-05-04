from behave import given, when, then


@given("Open Target main page for HW7")
def open_target_main_page_hw7(context):
    context.app.main_page.open_main()


@when("Click Account button for HW7")
def click_account_button_hw7(context):
    context.app.header.click_account()


@when("Click Sign In button from side navigation for HW7")
def click_sign_in_button_from_side_navigation_hw7(context):
    context.app.side_navigation_page.click_sign_in()


@then("Verify Sign In form opened for HW7")
def verify_sign_in_form_opened_hw7(context):
    context.app.sign_in_page.verify_sign_in_form_opened()


@when("Search for coffee for HW7")
def search_for_coffee_hw7(context):
    context.app.header.search_product("coffee")


@when("Add first product to cart for HW7")
def add_first_product_to_cart_hw7(context):
    context.app.search_results_page.add_first_product_to_cart()


@then("Verify product is in cart for HW7")
def verify_product_is_in_cart_hw7(context):
    context.app.cart_page.verify_product_in_cart()