from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then


BESTSELLER_LINKS = (By.CSS_SELECTOR, '._p13n-zg-nav-tab-all_style_zg-tabs__EYPLq li')


@when("Open Amazon BestSellers page")
def open_bestsellers_page(context):
    context.driver.get("https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers")


@then("User sees 5 links on page")
def links_on_page(context):
    links = context.driver.find_elements(*BESTSELLER_LINKS)
    assert len(links) == 5, "Expected 5 links but got {len(links}"
