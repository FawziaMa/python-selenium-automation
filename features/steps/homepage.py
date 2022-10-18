import time

from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


SIGN_IN_POPUP = (By.CSS_SELECTOR, '#nav-signin-tooltip .nav-action-inner' )


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')



@when('User clicks cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, ".nav-cart-icon").click()


@when('Click on button from SignIn PopUp')
def sign_in_popup(context):
    context.driver.wait.until(EC.element_to_be_clickable(SIGN_IN_POPUP), message="Sign in not clickable").click()


@then('Cart icon shows {expected_cart_count}')
def single_item_in_cart(context, expected_cart_count):
    actual_result = context.driver.find_element(By. ID, "nav-cart-count")
    assert actual_result == expected_cart_count 