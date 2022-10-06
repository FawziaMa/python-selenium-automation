import time

from selenium.webdriver.common.by import By
from behave import given, when, then


@when('User clicks Orders')
def click_orders(context):
    context.driver.find_element(By.XPATH, "//a[@class='nav-a nav-a-2   nav-progressive-attribute']").click()

