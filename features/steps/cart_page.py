from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then


@then('User sees {expected_result}')
def empty_cart_message(context, expected_result):
    actual_result = context.driver.find_element(By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']").text
    assert expected_result == actual_result, f'Error! Expected {expected_result}, but got {actual_result}'
