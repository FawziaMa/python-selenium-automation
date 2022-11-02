from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then


@when('{expected_results} shown')
def product_search_result(context, expected_results):
    actual_results = context.driver.find_element(By. XPATH, "//span[@class= 'a-color-state a-text-bold']").text
    assert expected_results == actual_results, f" Error expected {expected_results} but got {actual_results}"


@when("Add item to cart")
def add_product_to_cart(context):
    context.driver.find_element(By. XPATH, "//div[@class= 'a-row a-size-base a-color-base']").click()


