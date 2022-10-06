import time

from selenium.webdriver.common.by import By
from behave import given, when, then


@then('Sign in header and email input fields are visible')
def sign_in_ui(context):
    actual_result = context.driver.find_element(By.XPATH, "//h1[@class= 'a-spacing-small']").text
    expected_result = 'Sign in'
    assert expected_result == actual_result, f'Error: Expected {expected_result}, but got {actual_result}'

    actual_result = context.driver.find_element(By.XPATH, "//div[@class= 'a-row a-spacing-base']").text
    expected_result = 'Email or mobile phone number'
    assert expected_result == actual_result, f'Error: Expected {expected_result}, but got {actual_result}'
