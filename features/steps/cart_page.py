from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then


@then('User sees {expected_result}')
def empty_cart_message(context, expected_result):
    context.app.cart_page.empty_cart_message(expected_result)
