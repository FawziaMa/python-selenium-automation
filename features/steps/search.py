# from behave import *
# from selenium.webdriver.common.by import By
# import time
#
# SEARCH_RESULT = (By. CSS_SELECTOR, "[data-component-type='s-search-results']")
# PRODUCT_NAME = (By. CSS_SELECTOR, 'h2 span.a-size-base-plus')
# PRODUCT_IMAGE = (By. CSS_SELECTOR, 'span[data-component-type="s-product-image"]')
#
#
# @when("Input {listings} into search field")
# def input_search(context, listings):
#     search= context.driver.find_element(By. ID, "twotabsearchtextbox")
#     search.clear()
#     search.send_keys(listings)
#
#
# @When("Click on search icon")
# def click_search_icon(context):
#     context.driver.find_element(By. ID, "nav-search-submit-button").click()
#
#
# @then('Verify image and product name')
# def verify_name_and_image(context):
#     all_product = context.driver.find_elements(*SEARCH_RESULT)
#     for product in all_product:
#         title = product.find_element(*PRODUCT_NAME).text
#         assert title, 'Error, no title found'
#         product.find_element(*PRODUCT_IMAGE)
#
