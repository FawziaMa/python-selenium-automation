import time

from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


@then('Verify Amazon Privacy Notice page is opened')
def verify_privacy_page(context):
    context.driver.find_element(By. XPATH, "//h1[text()='Amazon.com Privacy Notice']")


@then('User can close new window and switch back to original')
def close_new_window(context):
    context.driver.close()


