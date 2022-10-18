from behave import *
from selenium.webdriver.common.by import By
import time


@when("Input {listings} into search field")
def input_search(context, listings):
    search= context.driver.find_element(By. ID, "twotabsearchtextbox")
    search.clear()
    search.send_keys(listings)
    time.sleep(5)


@When("Click on search icon")
def click_search_icon(context):
    context.driver.find_element(By. ID, "nav-search-submit-button").click()


