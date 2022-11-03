import time

from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

PRIVACY_LINK = (By. CSS_SELECTOR, 'a[href="https://www.amazon.com/privacy"]')


@given('Open T&C page')
def terms_conditions(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html?nodeId=GLSBYFE9MGKKQXXM')


@when('Store original windows')
def store_tc_window(context):
    context.original_window = context.driver.current_window_handle
    print('original', context.original_window)


@when('Click on Amazon Privacy Notice link')
def click_privacy_link(context):
    context.driver.find_element(*PRIVACY_LINK).click()


@when('Switch to the newly opened window')
def switch_to_new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    current_windows = context.driver.window_handles
    context.driver.switch_to.window(current_windows[1])