import time

from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


SIGN_IN_POPUP = (By.CSS_SELECTOR, '#nav-signin-tooltip .nav-action-inner' )


@given('Open Amazon page')
def open_amazon(context):
    context.app.main_page.open_main()


@when('User clicks cart icon')
def click_cart_icon(context):
    context.app.main_page.click_cart_icon()


@when('Click on button from SignIn PopUp')
def sign_in_popup(context):
    context.driver.wait.until(EC.element_to_be_clickable(SIGN_IN_POPUP), message="Sign in not clickable").click()


@when('User clicks Orders')
def click_orders(context):
    context.app.main_page.click_orders()


@when('Select department by value {selection_value}')
def select_department(context, selection_value):
    context.app.main_page.select_department(selection_value)


@then('Cart icon shows {expected_cart_count}')
def single_item_in_cart(context, expected_cart_count):
    actual_result = context.driver.find_element(By. ID, "nav-cart-count")
    assert actual_result == expected_cart_count
