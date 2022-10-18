from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

color_options = (By. CSS_SELECTOR, '#variation_color_name li')
current_color = (By. XPATH, "//div[@id='variation_color_name']//li[contains(@title,Click)]")


@given('Get {product_id} page')
def open_deal_page(context, product_id):
    context.driver.get(f'https://www.amazon.com/gp/product/{product_id}/')


@then('Verify color match description')
def verify_color_match(context):
    expected_colors = ['Click to select Black', 'Click to select Blue, Over Dye']

    actual_colors = []

    colors = context.driver.find_elements(*color_options)
    for color in colors:
        color.click()
        color_received = context.driver.find_elements(*current_color)
        actual_colors += [color_received]
    assert expected_colors == actual_colors
