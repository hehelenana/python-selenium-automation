from behave import given, when, then


@given("Open Target main page for HW6")
def open_target_main_page_hw6(context):
    context.app.main_page.open_main()


@when("Search for coffee for HW6")
def search_for_coffee_hw6(context):
    context.app.header.search_product("coffee")


@then("Verify search results for coffee shown for HW6")
def verify_search_results_for_coffee_hw6(context):
    context.app.search_results_page.verify_search_results("coffee")


@when("Click on Cart icon for HW6")
def click_on_cart_icon_hw6(context):
    context.app.header.click_cart_icon()


@then("Verify empty cart message is shown for HW6")
def verify_empty_cart_message_hw6(context):
    context.app.cart_page.verify_empty_cart_message()