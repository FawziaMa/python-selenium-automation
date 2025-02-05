from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

color_options = (By. CSS_SELECTOR, 'variation_color_name li')
current_color = (By. CSS_SELECTOR, 'variation_color_name li[title]')


@given('Get {product_id} page')
def open_deal_page(context, product_id):
    context.driver.get(f'https://www.amazon.com/gp/product/{product_id}/')


@given('User searches for product')
def search_for_product(context):
    context.driver.find_element(By.ID, '#twotabsearchtextbox').send_keys("coffee")



@then('Verify color match description')
def verify_color_match(context):
    expected_colors = ['Click to select Black',
                       'Click to select Blue, Over Dye',
                       'Click to select Dark Blue Vintage',
                       'Click to select Dark Indigo/Rinsed',]

    actual_colors = []

    colors = context.driver.find_elements(*color_options)
    for color in colors:
        color.click()
        color_received = context.driver.find_elements(*current_color)
        actual_colors += [color_received]
    assert expected_colors == actual_colors, f'Error'


