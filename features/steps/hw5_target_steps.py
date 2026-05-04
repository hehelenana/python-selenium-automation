from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

@given("I open the Target product page for HW5")
def open_target_product_page_hw5(context):
    context.driver.get("https://www.target.com/p/women-39-s-short-sleeve-ribbed-t-shirt-universal-thread-8482-cream-striped-3x/-/A-94836756")

    context.wait.until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Color')]"))
    )

@when("I click each available product color for HW5")
def click_each_available_product_color_hw5(context):
    color_links = context.wait.until(
        lambda driver: driver.find_elements(
            By.XPATH,
            "//a[contains(@aria-label, 'Color,')]"
        )
    )

    color_names = []

    for color_link in color_links:
        color_label = color_link.get_attribute("aria-label")
        color_name = color_label.replace("Color, ", "").replace(", selected", "")
        color_names.append(color_name)

    print("Colors found:", color_names)

    context.selected_colors = []

    for color_name in color_names:
        color_link = context.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, f"//a[contains(@aria-label, 'Color, {color_name}')]")
            )
        )

        print("Clicking color:", color_name)

        context.driver.execute_script("arguments[0].scrollIntoView(true);", color_link)
        context.driver.execute_script("arguments[0].click();", color_link)

        selected_color = context.wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    f"//a[contains(@aria-label, 'Color, {color_name}') and contains(@aria-label, 'selected')]"
                )
            )
        )

        selected_label = selected_color.get_attribute("aria-label")
        print("Selected color:", selected_label)

        context.selected_colors.append(selected_label)

@then("each color should be selected after clicking for HW5")
def verify_each_color_selected_hw5(context):
    print("Colors selected during test:", context.selected_colors)

    assert len(context.selected_colors) > 0