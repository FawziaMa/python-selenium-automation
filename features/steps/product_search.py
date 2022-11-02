from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_INPUT = (By. ID, "twotabsearchtextbox")
SEARCH_SUBMIT = (By.NAME, 'btnK')


#
#
# @given('Open Google page')
# def open_google(context):
#     context.driver.get('https://www.google.com/')


@when('Input {search_word} into search field')
def input_search(context, search_word):
    context.app.main_page.input_search(search_word)

    # search = context.driver.find_element(*SEARCH_INPUT)
    # search.clear()
    # search.send_keys(search_word)


@when('Click on search icon')
def click_search_icon(context):
    context.app.main_page.click_search_icon()


@then('Product results for {search_word} are shown')
def verify_found_results_text(context, search_word):
    assert search_word.lower() in context.driver.current_url.lower(), f"Expected query not in {context.driver.current_url.lower()}"
