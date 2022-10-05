import time

from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')
    time.sleep(20)


@when('User clicks cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, ".nav-cart-icon").click()
