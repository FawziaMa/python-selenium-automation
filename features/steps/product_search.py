from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_INPUT = (By. ID, "twotabsearchtextbox")
SEARCH_SUBMIT = (By.NAME, 'btnK')
SEARCH_RESULT = (By. CSS_SELECTOR, "[data-component-type='s-search-results']")
PRODUCT_NAME = (By. CSS_SELECTOR, 'h2 span.a-size-base-plus')
PRODUCT_IMAGE = (By. CSS_SELECTOR, 'span[data-component-type="s-product-image"]')


@when('Input {search_word} into search field')
def input_search(context, search_word):
    context.app.main_page.input_search(search_word)

    # search = context.driver.find_element(*SEARCH_INPUT)
    # search.clear()
    # search.send_keys(search_word)


@when('Click on search icon')
def click_search_icon(context):
    context.app.main_page.click_search_icon()


@given('Open {product} deal page')
def open_product_page(context, product):
    context.app.deal_page.open_product_page(product)


@when('User hovers over New Arrivals')
def hover_new_arrivals(context):
    context.app.deal_page.hover_new_arrivals()


@then('Product results for {search_word} are shown')
def verify_found_results_text(context, search_word):
    assert search_word.lower() in context.driver.current_url.lower(), f"Expected query not in {context.driver.current_url.lower()}"


@then('Verify image and product name')
def verify_name_and_image(context):
    all_product = context.driver.find_elements(*SEARCH_RESULT)
    for product in all_product:
        title = product.find_element(*PRODUCT_NAME).text
        assert title, 'Error, no title found'
        product.find_element(*PRODUCT_IMAGE)


@then('Verify deals are shown')
def verify_new_arrival_deals(context):
    context.app.deal_page.verify_new_arrival_deals()

